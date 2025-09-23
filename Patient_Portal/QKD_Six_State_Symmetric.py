import numpy as np
import random
import os
import time

class QKD:
    # Initiate Qubits
    _k1 = 1.0 / 2.0
    _k2 = np.sqrt(3.0) / 2.0

    A_kets = [np.array([1.0, 0.0], dtype=complex), np.array([0.0, 1.0], dtype=complex)]
    B_kets = [np.array([_k1, -_k2], dtype=complex), np.array([_k2, _k1], dtype=complex)]
    C_kets = [np.array([-_k1, -_k2], dtype=complex), np.array([_k2, -_k1], dtype=complex)]

    BASIS_KETS = {
        0: A_kets,
        1: B_kets,
        2: C_kets
    }

    def __init__(self, size_tx: int, filepath: str, noise_prob: float = 0.0):
        self.SIZE_TX = size_tx
        self.filepath = filepath
        self.noise_prob = noise_prob

        # For Alice variables
        self.state_matrix = np.zeros((2, size_tx), dtype=complex)
        self.encoded_msg = []
        self.basis_seq_a = np.zeros(size_tx, dtype=int)
        self.states_seq_a = np.zeros(size_tx, dtype=int)
        self.msg_length = 0

        # For Bob variables
        self.meas_seq_b = np.zeros(size_tx, dtype=int)
        self.basis_seq_b = np.zeros(size_tx, dtype=int)

        # Quantum Channel variables
        self.st_mtx_in = None
        self.out_st_mtx = None

    # Cipher text file (file to bits)
    def file_to_bits(filepath: str) -> str:
        with open(filepath, "rb") as f:   # open as binary
            data = f.read()
        return ''.join(f"{byte:08b}" for byte in data)

    # bits to file
    def bits_to_file(bits: str, output_path: str):
        if len(bits) % 8 != 0:
            raise ValueError("Bit string length is not multiple of 8")
        byte_array = bytearray(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
        with open(output_path, "wb") as f:
            f.write(byte_array)
        return output_path

    # Encryption proc
    def qkd_encrypt_file(filepath):
        bitstring = QKD.file_to_bits(filepath)
        
        # print("Classical Bits Before Transmission (first 128 bits):", bitstring[:128])

        bases = np.random.randint(0, 3, size=len(bitstring))
        encoded = []
        for bit_char, basis in zip(bitstring, bases):
            if basis == 0:
                encoded.append(int(bit_char))
            elif basis == 1:
                encoded.append("2" if bit_char == "0" else "3")
            else:
                encoded.append("4" if bit_char == "0" else "5")
        return encoded, bases, len(bitstring)

    # Decryption Proc
    def qkd_decrypt_file(encoded, bases):
        bits = []
        for symbol, basis in zip(encoded, bases):
            if basis == 0:
                bits.append(symbol if isinstance(symbol, str) else str(symbol))
            elif basis == 1:
                bits.append("0" if symbol == "2" else "1")
            elif basis == 2:
                bits.append("0" if symbol == "4" else "1")
        return ''.join(bits)

    # Reencrypt process
    def symbol_to_state(symbol, basis):
        if basis == 0:
            return int(symbol)
        elif basis == 1:
            return 0 if symbol == "2" else 1
        elif basis == 2:
            return 0 if symbol == "4" else 1
        else:
            raise ValueError("Invalid basis in symbol_to_state()")

    # Alice Preparation
    def seq_init_alice_from_file(self):
        encoded, bases, self.msg_length = QKD.qkd_encrypt_file(self.filepath)
        if len(encoded) > self.SIZE_TX:
            raise ValueError("Message too long for allocated qubits!")
        self.encoded_msg = encoded
        self.basis_seq_a[:self.msg_length] = bases
        for i, sym in enumerate(self.encoded_msg):
            self.states_seq_a[i] = QKD.symbol_to_state(sym, int(self.basis_seq_a[i]))
        # print(self.states_seq_a)

    # Alice to generate qubits based on the bits 
    def generate_qubit_stream(self):
        for i in range(self.msg_length):
            b = int(self.basis_seq_a[i])
            s = int(self.states_seq_a[i])
            self.state_matrix[:, i] = QKD.BASIS_KETS[b][s]

    # Quantum Channel Simu (with error prob)
    def transmit_channel(self):
        self.st_mtx_in = self.state_matrix
        if random.random() < self.noise_prob:
            # To have the same size
            self.out_st_mtx = np.copy(self.st_mtx_in)
            for q in range(self.st_mtx_in.shape[1]):
                if random.random() < self.noise_prob:
                    column = self.out_st_mtx[:, q]
                    # Compare and flip between paired kets
                    if np.allclose(column, self.A_kets[0]):
                        self.out_st_mtx[:, q] = QKD.A_kets[1]
                    elif np.allclose(column, self.A_kets[1]):
                        self.out_st_mtx[:, q] = QKD.A_kets[0]
                    elif np.allclose(column, self.B_kets[0]):
                        self.out_st_mtx[:, q] = QKD.B_kets[1]
                    elif np.allclose(column, self.B_kets[1]):
                        self.out_st_mtx[:, q] = QKD.B_kets[0]
                    elif np.allclose(column, self.C_kets[0]):
                        self.out_st_mtx[:, q] = QKD.C_kets[1]
                    elif np.allclose(column, self.C_kets[1]):
                        self.out_st_mtx[:, q] = QKD.C_kets[0]
        else:
            self.out_st_mtx = self.st_mtx_in

    # Bob preparation
    def seq_init_bob(self):
        self.basis_seq_b = np.random.randint(low=0, high=3, size=self.SIZE_TX)
        self.meas_seq_b = np.zeros(self.SIZE_TX, dtype=int)

    # Bob measurement
    def meas_qubit_stream_bob(self):
        for j in range(self.SIZE_TX):
            st = self.out_st_mtx[:, j].astype(complex)
            b = int(self.basis_seq_b[j])
            ket0 = QKD.BASIS_KETS[b][0]
            p0 = np.abs(np.vdot(ket0, st))**2
            p0 = min(max(p0.real, 0.0), 1.0)
            self.meas_seq_b[j] = 0 if random.random() < p0 else 1
        return self.meas_seq_b

    # Decryption
    def decrypt_from_measurement(self):
        num_columns_mat = self.out_st_mtx.shape[1]
        decodedBit, decodedBases = [], []
        for q in range(num_columns_mat):
            column = self.out_st_mtx[:, q]
            # Compare and flip between paired kets
            if np.allclose(column, QKD.A_kets[0]):
                decodedBit.append("0")
                decodedBases.append(0)
            elif np.allclose(column, QKD.A_kets[1]):
                decodedBit.append("1")
                decodedBases.append(0)
            elif np.allclose(column, QKD.B_kets[0]):
                decodedBit.append("2")
                decodedBases.append(1)
            elif np.allclose(column, QKD.B_kets[1]):
                decodedBit.append("3")
                decodedBases.append(1)
            elif np.allclose(column, QKD.C_kets[0]):
                decodedBit.append("4")
                decodedBases.append(2)
            elif np.allclose(column, QKD.C_kets[1]):
                decodedBit.append("5")
                decodedBases.append(2)
        
        try:
            bitstring = QKD.qkd_decrypt_file(decodedBit, decodedBases[:len(decodedBit)])
            # print("Classical Bits After Transmission (first 128 bits):", bitstring[:128])

            output_path = "Recovered_Medical_Report.pdf"
            QKD.bits_to_file(bitstring, output_path)
            
            print("\n===============================================================================")
            print("Bob reconstructed file:", output_path)
            print("===============================================================================")
            return output_path
        except Exception as e:
            print("Decoding failed:", e)
            return None

    
    # Experiment initiate
    def execute(self):
        self.seq_init_alice_from_file()
        self.generate_qubit_stream()
        self.transmit_channel()
        self.seq_init_bob()
        self.meas_qubit_stream_bob()
        return self.decrypt_from_measurement()

    def final(self):
        recovered_path = self.execute()
        if recovered_path and os.path.exists(recovered_path):
            return recovered_path
        else:
            print("\n Recovery failed. Bits corrupted")


# def main():
#     SIZE_TX = 1000000
#     pdf_path = "MRI BRAIN W_O CONTRAST.pdf"
#     noise = 0.0
#     simuStart =time.time() # To calculate time
#     qkd = QKD(SIZE_TX, pdf_path, noise)
#     qkd.final()
#     simuEnd = time.time()
#     print("Execution time:", simuEnd - simuStart, "seconds")


# if __name__ == '__main__':
#     main()
