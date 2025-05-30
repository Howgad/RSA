import unittest
from RSA_Cipher.rsa import generate_keypair, encrypt, decrypt

class TestRSA(unittest.TestCase):

    def test_rsa_encrypt_decrypt(self):
        pub, priv = generate_keypair()
        msg = "HelloRSA"
        encrypted = encrypt(pub, msg)
        decrypted = decrypt(priv, encrypted)
        self.assertEqual(decrypted, msg)

    def test_different_keys(self):
        pub1, priv1 = generate_keypair()
        pub2, priv2 = generate_keypair()
        msg = "Data"
        self.assertNotEqual(encrypt(pub1, msg), encrypt(pub2, msg))

    def test_inverse_encryption(self):
        pub, priv = generate_keypair()
        msg = "Test"
        ciphertext = encrypt(pub, msg)
        self.assertEqual(decrypt(priv, ciphertext), msg)

if __name__ == '__main__':
    unittest.main()