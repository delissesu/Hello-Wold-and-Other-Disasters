def get_user_ingredients():
    user_input = input("Masukkan bahan yang Anda miliki (pisahkan dengan koma): ")
    
    # Hapus spasi ekstra dan ubah ke lowercase untuk konsistensi
    ingredients = set(ingredient.strip().lower() for ingredient in user_input.split(","))
    return ingredients

def check_ingredients(recipe_ingredients, user_ingredients):
    # Bahan yang dibutuhkan tapi tidak dimiliki user
    missing = recipe_ingredients - user_ingredients
    
    # Bahan yang dimiliki user tapi tidak dibutuhkan resep
    extra = user_ingredients - recipe_ingredients
    
    return missing, extra

def print_results(missing_ingredients, extra_ingredients):
    print("\n" + "=" * 50)
    print("HASIL PENGECEKAN BAHAN".center(50))
    print("=" * 50)
    
    # Tampilkan bahan yang kurang
    if missing_ingredients:
        missing_list = ", ".join(missing_ingredients)
        print(f"Bahan yang kurang: {missing_list}")
    else:
        print("Semua bahan tersedia!")
    
    # Tampilkan bahan berlebih
    if extra_ingredients:
        extra_list = ", ".join(extra_ingredients)
        print(f"ℹBahan berlebih: {extra_list}")
    
    print("=" * 50)

def main():
    # Daftar bahan yang dibutuhkan untuk resep
    RECIPE_INGREDIENTS = {"flour", "sugar", "milk", "eggs"}
    
    print("PROGRAM PENGECEKAN BAHAN MASAK")
    print(f"Bahan yang dibutuhkan: {', '.join(RECIPE_INGREDIENTS)}")
    print("-" * 50)
    
    # Ambil input dari user
    user_ingredients = get_user_ingredients()
    
    # Cek bahan yang kurang dan berlebih
    missing, extra = check_ingredients(RECIPE_INGREDIENTS, user_ingredients)
    
    # Tampilkan hasil
    print_results(missing, extra)
    
    # Kesimpulan akhir
    if not missing:
        print("🎉 Selamat! Anda bisa mulai memasak!")
    else:
        print("🛒 Silakan beli bahan yang kurang terlebih dahulu.")

if __name__ == "__main__":
    main()