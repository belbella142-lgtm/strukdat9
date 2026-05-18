"""
====================================================
  PROGRAM ALGORITMA BACKTRACKING
  Menggabungkan 3 masalah klasik:
    1. N-Queens (N-Ratu)
    2. Knight's Tour (Tur Kuda)
    3. Knapsack (Tas Ransel)
====================================================
"""

#  BAGIAN 1: N-QUEENS

def nq_print_board(board, n):
    print("\n+" + "---+" * n)
    for row in range(n):
        line = "|"
        for col in range(n):
            line += " Q |" if board[row] == col else "   |"
        print(line)
        print("+" + "---+" * n)
    print()


def nq_is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if board[i] - col == i - row:
            return False
        if board[i] - col == row - i:
            return False
    return True


def nq_solve(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if nq_is_safe(board, row, col):
            board[row] = col
            nq_solve(board, row + 1, n, solutions)
            board[row] = -1


def run_n_queens():
    print("\n" + "=" * 50)
    print("   PROGRAM 1: N-QUEENS (N-RATU)")
    print("=" * 50)

    while True:
        try:
            n = int(input("\nMasukkan ukuran papan (N): "))
            if n < 1:
                print("Ukuran papan harus minimal 1.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

    board = [-1] * n
    solutions = []
    print(f"\nMencari solusi untuk {n}-Queens...")
    nq_solve(board, 0, n, solutions)

    if not solutions:
        print(f"\nTidak ada solusi untuk {n}-Queens.")
    else:
        print(f"\nDitemukan {len(solutions)} solusi!")
        show_all = input("\nTampilkan semua solusi? (y/n): ").strip().lower()
        if show_all == 'y':
            for idx, sol in enumerate(solutions, 1):
                print(f"\n--- Solusi {idx} ---")
                nq_print_board(sol, n)
        else:
            print("\n--- Solusi Pertama ---")
            nq_print_board(solutions[0], n)

        print(f"Total solusi ditemukan: {len(solutions)}")
        print("Posisi ratu per baris (kolom dimulai dari 0):")
        for idx, sol in enumerate(solutions[:3], 1):
            print(f"  Solusi {idx}: {sol}")
        if len(solutions) > 3:
            print(f"  ... dan {len(solutions) - 3} solusi lainnya")


#  BAGIAN 2: KNIGHT'S TOUR

KT_MOVE_X = [2, 1, -1, -2, -2, -1,  1,  2]
KT_MOVE_Y = [1, 2,  2,  1, -1, -2, -2, -1]


def kt_print_board(board, n):
    cell_width = len(str(n * n)) + 1
    separator = "+" + ("-" * cell_width + "+") * n
    print("\n" + separator)
    for row in range(n):
        line = "|"
        for col in range(n):
            line += str(board[row][col]).center(cell_width) + "|"
        print(line)
        print(separator)
    print()


def kt_is_valid(x, y, board, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1


def kt_get_degree(x, y, board, n):
    return sum(
        1 for i in range(8)
        if kt_is_valid(x + KT_MOVE_X[i], y + KT_MOVE_Y[i], board, n)
    )


def kt_solve(board, x, y, move_count, n, path):
    if move_count == n * n:
        return True

    moves = []
    for i in range(8):
        nx, ny = x + KT_MOVE_X[i], y + KT_MOVE_Y[i]
        if kt_is_valid(nx, ny, board, n):
            moves.append((kt_get_degree(nx, ny, board, n), nx, ny))

    moves.sort(key=lambda m: m[0])

    for _, nx, ny in moves:
        board[nx][ny] = move_count
        path.append((nx, ny))
        if kt_solve(board, nx, ny, move_count + 1, n, path):
            return True
        board[nx][ny] = -1
        path.pop()

    return False


def run_knights_tour():
    print("\n" + "=" * 50)
    print("   PROGRAM 2: TUR KUDA (KNIGHT'S TOUR)")
    print("=" * 50)

    while True:
        try:
            n = int(input("\nMasukkan ukuran papan (N, min 5 disarankan): "))
            if n < 1:
                print("Ukuran papan harus minimal 1.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

    while True:
        try:
            sr = int(input(f"Masukkan baris awal kuda (0-{n-1}): "))
            sc = int(input(f"Masukkan kolom awal kuda (0-{n-1}): "))
            if not (0 <= sr < n and 0 <= sc < n):
                print(f"Posisi harus antara 0 dan {n-1}.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

    board = [[-1] * n for _ in range(n)]
    board[sr][sc] = 0
    path = [(sr, sc)]

    print(f"\nMencari solusi Tur Kuda pada papan {n}x{n}...")
    print(f"Posisi awal: ({sr}, {sc})")
    print("Menggunakan Warnsdorff's Heuristic...\n")

    if kt_solve(board, sr, sc, 1, n, path):
        print("✓ Solusi ditemukan!\n")
        kt_print_board(board, n)
        print("Daftar langkah Tur Kuda:")
        print(f"{'Langkah':<10} {'Posisi (baris, kolom)'}")
        print("-" * 35)
        for step, (r, c) in enumerate(path):
            print(f"  {step + 1:<8} ({r}, {c})")
    else:
        print("✗ Tidak ada solusi dari posisi ini. Coba posisi lain.")


#  BAGIAN 3: KNAPSACK

def ks_solve(items, weights, target, index, current_weight, current_items, all_solutions):
    if current_weight == target:
        all_solutions.append((list(current_items), current_weight))
        return
    if index == len(weights):
        return
    if current_weight + weights[index] > target:
        ks_solve(items, weights, target, index + 1,
                 current_weight, current_items, all_solutions)
        return

    # Masukkan barang
    current_items.append(items[index])
    ks_solve(items, weights, target, index + 1,
             current_weight + weights[index], current_items, all_solutions)
    current_items.pop()

    # Lewati barang
    ks_solve(items, weights, target, index + 1,
             current_weight, current_items, all_solutions)


def ks_closest(items, weights, target):
    best = [[], 0]

    def backtrack(index, current_weight, current_items):
        if current_weight > best[1]:
            best[0] = list(current_items)
            best[1] = current_weight
        if index == len(weights):
            return
        for i in range(index, len(weights)):
            if current_weight + weights[i] <= target:
                current_items.append(items[i])
                backtrack(i + 1, current_weight + weights[i], current_items)
                current_items.pop()

    backtrack(0, 0, [])
    return best[0], best[1]


def run_knapsack():
    print("\n" + "=" * 55)
    print("   PROGRAM 3: KNAPSACK (MASALAH TAS RANSEL)")
    print("=" * 55)

    print("\nPilih mode input:")
    print("  1. Gunakan contoh soal (7 barang, target 30 pon)")
    print("  2. Masukkan data sendiri")

    while True:
        choice = input("\nPilihan (1/2): ").strip()
        if choice in ['1', '2']:
            break
        print("Pilihan tidak valid.")

    if choice == '1':
        items   = ["Barang-1","Barang-2","Barang-3","Barang-4",
                   "Barang-5","Barang-6","Barang-7"]
        weights = [2, 5, 6, 9, 12, 14, 20]
        target  = 30
        print(f"\nData contoh: berat = {weights}, target = {target} pon")
    else:
        items, weights = [], []
        item_num = 1
        print("\nMasukkan data barang (ketik 'selesai' untuk berhenti):")
        while True:
            name = input(f"  Nama barang {item_num} (atau 'selesai'): ").strip()
            if name.lower() == 'selesai':
                if not items:
                    print("  Minimal masukkan 1 barang.")
                    continue
                break
            try:
                w = float(input(f"  Berat '{name}': "))
                if w <= 0:
                    print("  Berat harus > 0.")
                    continue
                items.append(name)
                weights.append(w)
                item_num += 1
            except ValueError:
                print("  Input tidak valid.")

        while True:
            try:
                target = float(input("\nMasukkan berat target: "))
                if target > 0:
                    break
                print("Berat target harus > 0.")
            except ValueError:
                print("Input tidak valid.")

    print(f"\n{'No':<5} {'Nama Barang':<20} {'Berat':>10}")
    print(f"{'-'*5} {'-'*20} {'-'*10}")
    for i, (item, w) in enumerate(zip(items, weights), 1):
        print(f"{i:<5} {item:<20} {w:>10.1f}")
    print(f"\nBerat Target : {target}")

    print(f"\nMencari kombinasi dengan total berat tepat = {target}...")
    all_solutions = []
    ks_solve(items, weights, target, 0, 0, [], all_solutions)

    if all_solutions:
        print(f"\n✓ Ditemukan {len(all_solutions)} solusi!\n")
        for idx, (sol_items, sol_weight) in enumerate(all_solutions, 1):
            sol_w = [weights[items.index(it)] for it in sol_items]
            print(f"Solusi {idx}:")
            print(f"  Barang : {sol_items}")
            print(f"  Berat  : {sol_w}")
            print(f"  Total  : {sol_weight}\n")
    else:
        print(f"\n✗ Tidak ada kombinasi tepat = {target}.")
        print("Mencari kombinasi yang paling mendekati...")
        best_items, best_weight = ks_closest(items, weights, target)
        if best_items:
            best_w = [weights[items.index(it)] for it in best_items]
            print(f"\n  Kombinasi terbaik:")
            print(f"  Barang : {best_items}")
            print(f"  Berat  : {best_w}")
            print(f"  Total  : {best_weight} (target: {target})")
        else:
            print("  Tidak ada barang yang bisa dimasukkan.")


# ============================================================
#  MENU UTAMA
# ============================================================

def main():
    while True:
        print("\n" + "=" * 50)
        print("   ALGORITMA BACKTRACKING - MENU UTAMA")
        print("=" * 50)
        print("  1. N-Queens (N-Ratu)")
        print("  2. Knight's Tour (Tur Kuda)")
        print("  3. Knapsack (Tas Ransel)")
        print("  0. Keluar")
        print("=" * 50)

        pilihan = input("Pilih program (0-3): ").strip()

        if pilihan == '1':
            run_n_queens()
        elif pilihan == '2':
            run_knights_tour()
        elif pilihan == '3':
            run_knapsack()
        elif pilihan == '0':
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Masukkan 0, 1, 2, atau 3.")

        input("\nTekan Enter untuk kembali ke menu...")


if __name__ == "__main__":
    main()
