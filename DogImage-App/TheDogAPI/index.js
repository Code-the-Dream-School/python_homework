const dogOutput = document.getElementById("dog-output");
const newDogBtn = document.getElementById("new-dog-btn");
const navRandomBtn = document.getElementById("nav-random");
const navBreedsBtn = document.getElementById("nav-breeds");

function fetchRandomDog() {
  fetch("https://api.thedogapi.com/v1/images/search")
    .then(response => response.json())
    .then(data => {
      const dog = data[0];
      const breedName = dog.breeds?.[0]?.name || "Unknown Breed";

      dogOutput.innerHTML = `
        <img src="${dog.url}" alt="A random dog" width="300"/>
        <p><strong>Breed:</strong> ${breedName}</p>
      `;
    })
    .catch(error => {
      dogOutput.innerHTML = "<p>Sorry, something went wrong fetching the dog.</p>";
      console.error(error);
    });
}

function fetchBreeds() {
  fetch("https://api.thedogapi.com/v1/breeds")
    .then(res => res.json())
    .then(data => {
      const breedListHTML = data.map(breed => `
        <div class="breed-card">
          <h3>${breed.name}</h3>
          <p><strong>Temperament:</strong> ${breed.temperament || "N/A"}</p>
          <p><strong>Life Span:</strong> ${breed.life_span}</p>
          <button onclick="fetchBreedImage(${breed.id}, '${breed.name.replace(/'/g, "\\'")}')">Show Image</button>
        </div>
      `).join("");
      dogOutput.innerHTML = `<h2>Explore Dog Breeds</h2>${breedListHTML}`;
    })
    .catch(error => {
      dogOutput.innerHTML = "<p>Sorry, couldn't fetch breed list.</p>";
      console.error(error);
    });
}

function fetchBreedImage(breedId, breedName) {
  fetch(`https://api.thedogapi.com/v1/images/search?breed_id=${breedId}`)
    .then(res => res.json())
    .then(data => {
      const img = data[0]?.url || "";
      dogOutput.innerHTML = `
        <h2>${breedName}</h2>
        <img src="${img}" alt="${breedName}" />
        <button onclick="fetchBreeds()">Back to Breeds</button>
      `;
    })
    .catch(error => {
      dogOutput.innerHTML = "<p>Sorry, couldn't fetch image.</p>";
      console.error(error);
    });
}

// Navigation handlers
newDogBtn.addEventListener("click", fetchRandomDog);

navRandomBtn.addEventListener("click", () => {
  fetchRandomDog();
  newDogBtn.style.display = "inline-block";
});

navBreedsBtn.addEventListener("click", () => {
  fetchBreeds();
  newDogBtn.style.display = "none";
});

// Load random dog on first visit
fetchRandomDog();


