import client
import server


def gen_keys():
    return client.client_key(), server.server_key()


def main():
    ck, sk = gen_keys()

    cipher_text1 = ck.encrypt(True)
    cipher_text2 = ck.encrypt(False)

    cipher_text3 = sk.hom_not(cipher_text2)
    cipher_text4 = sk.hom_and(cipher_text1, cipher_text2)
    cipher_text5 = sk.hom_nand(cipher_text3, cipher_text4)
    cipher_text6 = sk.hom_mux(cipher_text5, cipher_text3, cipher_text4)

    dec_output = ck.decrypt(cipher_text6)
    assert dec_output == True, "計算結果があってないぞ><"

if __name__ == '__main__':
    main()
