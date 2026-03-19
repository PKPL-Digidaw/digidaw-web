const anggota = [
    {
        nama: "Vidya Pramudita Andini",
        npm: "2406432513",
        role: "Frontend Developer",
        foto: "https://i.pravatar.cc/100?img=1"
    },
    {
        nama: "Afifah Widhia Rahayu",
        npm: "2406402662",
        role: "Backend Developer",
        foto: "https://i.pravatar.cc/100?img=2"
    },
    {
        nama: "Dhea Anggrayningsih Syah Roni",
        npm: "2406437262",
        role: "OAuth Engineer",
        foto: "https://i.pravatar.cc/100?img=3"
    },
    {
        nama: "Levina Aurellia",
        npm: "2406356776",
        role: "Backend Engineer",
        foto: "https://i.pravatar.cc/100?img=4"
    },
    {
        nama: "Nadine Aisyah Putri Maharani",
        npm: "2406408224",
        role: "OAuth Engineer",
        foto: "https://i.pravatar.cc/100?img=5"
    }
];

const container = document.getElementById("biodataContainer");

// render card
anggota.forEach((item) => {
    const card = document.createElement("div");
    card.className = "card";

   card.innerHTML = `
        <img src="${item.foto}">
        <h3>${item.nama}</h3>
        <p class="npm">NPM: ${item.npm}</p>
        <p class="role">${item.role}</p>
        <span class="tag">DIGIDAW TEAM</span>
    `;

    container.appendChild(card);
});

// login button (placeholder OAuth)
document.getElementById("loginBtn").addEventListener("click", () => {
    alert("Login dengan Google akan diintegrasikan di sini 🚀");
});