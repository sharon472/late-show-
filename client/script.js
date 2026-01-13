const BASE = "http://127.0.0.1:5000";

// -----------------------
// Load Episodes
// -----------------------
async function loadEpisodes() {
  try {
    const res = await fetch(`${BASE}/episodes`);
    const data = await res.json();
    const ul = document.getElementById("episodes");
    ul.innerHTML = ""; // clear existing
    data.forEach(ep => {
      const li = document.createElement("li");
      li.textContent = `Episode ${ep.number} - ${ep.date}`;
      ul.appendChild(li);
    });
  } catch (err) {
    console.error("Error loading episodes:", err);
  }
}

// -----------------------
// Load Guests
// -----------------------
async function loadGuests() {
  try {
    const res = await fetch(`${BASE}/guests`);
    const data = await res.json();
    const ul = document.getElementById("guests");
    ul.innerHTML = ""; // clear existing
    data.forEach(g => {
      const li = document.createElement("li");
      li.textContent = `${g.name} (${g.occupation})`;
      ul.appendChild(li);
    });
  } catch (err) {
    console.error("Error loading guests:", err);
  }
}

// -----------------------
// Create Appearance
// -----------------------
document.getElementById("form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const rating = parseInt(document.getElementById("rating").value);
  const episode_id = parseInt(document.getElementById("episode_id").value);
  const guest_id = parseInt(document.getElementById("guest_id").value);

  try {
    const res = await fetch(`${BASE}/appearances`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ rating, episode_id, guest_id })
    });

    const data = await res.json();
    document.getElementById("result").textContent = JSON.stringify(data, null, 2);

    // Reload episodes and guests in case of new changes
    loadEpisodes();
    loadGuests();

    // Reset form
    e.target.reset();
  } catch (err) {
    console.error("Error creating appearance:", err);
  }
});

// -----------------------
// Initial Load
// -----------------------
loadEpisodes();
loadGuests();
