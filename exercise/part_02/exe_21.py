def Tao_In_DS():
    ds = []
    for i in range(1, 21):
        ds.append(i ** 2)
    print(ds)
    print("5 phần tử đầu + 5 phần tử cuối:", ds[0:5] + ds[-5:])
    print(f"5 phần tử đầu {ds[0:5]} và 5 phần tử cuối {ds[-5:]}")

Tao_In_DS()
