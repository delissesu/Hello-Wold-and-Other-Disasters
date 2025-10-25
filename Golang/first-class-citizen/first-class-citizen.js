// Kemampuan untuk memperlakukan fungsi sebagai nilai
let greet = function() {
    console.log("Naveria Works")
}

greet()

// Kemampuan untuk meneruskan fungsi sebagai argumen
function waifu1() {
    return "Chinatsu Kano"
}

function waifu2() {
    return "Anzu Hanashiro"
}

function myKisah(waifu) {
    console.log("Halo mY", waifu())
}

let istri_pertama = myKisah(waifu1)
let istri_kedua = myKisah(waifu2)

// Kemampuan untuk mengembalikan fungsi dari fungsi lain
let getNama = function() {
    return function() {
        console.log("Halo Kingg!")
    }
}

// Tanda kurung pertama merujuk ke fungsi anonim yang pertama, tepatnya ke fungsi itu sendiri.
// Tanda kurung kedua merujuk ke fungsi yang dikembalikan, yaitu fungsi anonim yang menyetak ke konsol
getNama()()

// Contoh Lain 1
let getNama1 = function() {
    return function() {
        console.log("Halo King!")
    }
}

// 1. Jalankan fungsi luar dan kemudian simpan hasilnya
let fungsiYangDikembalikan = getNama1()

// 2. Jalankan fungsi yang sudah disimpan
fungsiYangDikembalikan() 

// Contoh lain 2
function buatSapaan(salam) {
    let fungsiSapaan = function(nama) {
        console.log(`Halo, ${salam} Kak ${nama}!`)
    }
    
    return fungsiSapaan
}

let sapaan_pagi = buatSapaan("Selamat Pagi")
let sapaan_malam = buatSapaan("Selamat Malam")

sapaan_pagi("Kano")
sapaan_malam("Anzu")

// Panggil fungsi secara lansgung
buatSapaan("Woiii!")("Liaaa") // Pertama akan mengisi parameter salam dan dilanjutkan dengan parameter nama.