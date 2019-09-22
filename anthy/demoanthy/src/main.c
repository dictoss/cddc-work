#include <stdlib.h>
#include <stdio.h>
#include <anthy/anthy.h>

/* function */
void demo_call_anthy(anthy_context_t ac);

/*
 * main
 */
int main(int argc, char *argv[])
{
    int ret = 0;
    anthy_context_t ac;

    ret = anthy_init();
    if(ret < 0){
        return EXIT_FAILURE;
    }

    /* init anthy */
    ac = anthy_create_context();
    anthy_context_set_encoding(ac, ANTHY_UTF8_ENCODING);

    /* call demo */
    fprintf(stderr, "anthy version: %s\n", anthy_get_version_string());
    demo_call_anthy(ac);

    /* crelease anthy */
    anthy_release_context(ac);
    anthy_quit();
    
    return EXIT_SUCCESS;
}


void demo_call_anthy(anthy_context_t ac)
{
    int ret = 0;
    int i = 0;
    int len_bytes = 0;
    int condidate = 0;
    /* 入力がローマ字だと変換できないので、何か処理が足りないのだろう。。。 */
    /* const char *in_str = "kyounoohiruhatabemashitaka"; */
    const char *in_str = "きょうのひるはたべましたか";
    struct anthy_conv_stat acs = {0};
    char buf[1024];

    fprintf(stderr, "IN  %s()\n", __func__);

    ret =  anthy_set_string(ac, in_str);
    fprintf(stderr, "anthy_set_string() : ret = %d, in_str = %s\n", ret, in_str);
    /* anthy_print_context(ac); */

    ret = anthy_get_stat(ac, &acs);
    fprintf(stderr, "anthy_get_stat() : ret = %d, nr_segment = %d\n", ret, acs.nr_segment);

    /*
      今回は予測変換の第1候補で変換するため、condidate = 0を指定。
      そのほかに以下の値を指定可能。
        anthy.h:39:#define NTH_UNCONVERTED_CANDIDATE -1
        anthy.h:40:#define NTH_KATAKANA_CANDIDATE -2
        anthy.h:41:#define NTH_HIRAGANA_CANDIDATE -3
        anthy.h:42:#define NTH_HALFKANA_CANDIDATE -4
     */
    condidate = 0;

    for(i = 0; i < acs.nr_segment; i ++){
        len_bytes = anthy_get_segment(ac, i, condidate, buf, sizeof(buf)); 
        fprintf(stderr, "  anthy_get_segment() : len_bytes = %d, buf = %s\n", len_bytes, buf);

        if(len_bytes < 0){
            break;
        }
    }

    fprintf(stderr, "OUT %s()\n", __func__);
}
