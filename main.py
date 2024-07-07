
def draw_triangle(n: int) -> list:
    """
    Returns the pascal triangle with n rows
    """
    assert n < 0 : ValueError
    row = [[1]]
    for i in range(1, n):
        new_row = [1]
        for j in range(2, i):
            new_row.append(row[i - 1][j - 2] + row[i - 1][j - 1])
        row.append(new_row)
    return row


def main():
    draw_triangle()


if __name__ == "__main__":
    print("Dibujando el triangulo de Pascal")
    main()

