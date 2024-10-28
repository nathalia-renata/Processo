
def elemento():
    seq_a = [1, 3, 5, 7]
    seq_a.append(seq_a[-1] + 2)  
    print(f"a) {seq_a}")

    seq_b = [2, 4, 8, 16, 32, 64]
    seq_b.append(seq_b[-1] * 2)  
    print(f"b) {seq_b}")

    
    seq_c = [0, 1, 4, 9, 16, 25, 36]
    seq_c.append(len(seq_c) ** 2)  
    print(f"c) {seq_c}")

    
    seq_d = [4, 16, 36, 64]
    seq_d.append((len(seq_d) + 1) * 2 ** 2)  
    print(f"d) {seq_d}")

    
    seq_e = [1, 1, 2, 3, 5, 8]
    seq_e.append(seq_e[-1] + seq_e[-2])  
    print(f"e) {seq_e}")

   
    seq_f = [2, 10, 12, 16, 17, 18, 19]
    seq_f.append(20)  
    print(f"f) {seq_f}")

if __name__ == "__main__":
    elemento()

#o resulado é a)9 B)128 c)49 d)20, E) 13, f) 20
