// Pick which version to use: SHA preferred, fallback to branch, then latest
const baseURL = 'https://alisaifee.github.io/py-benchmark-docs/';
const tryURLs = [
  `${baseURL}/${BENCH_GITSHA}/summary.json`,
  `${baseURL}/${BENCH_BRANCH}/summary.json`,
];

function fetchWithFallback(urls) {
  const [head, ...tail] = urls;
  return fetch(head)
    .then(res => {
      if (!res.ok) throw new Error("Next");
      return res.json();
    })
    .catch(() => {
      if (tail.length === 0) throw new Error("No valid benchmark JSON found");
      return fetchWithFallback(tail);
    });
}
fetchWithFallback(tryURLs)
  .then(data => {
    const displayEl = document.getElementById("benchmark-data");
    if (displayEl) {
      displayEl.textContent = JSON.stringify(data, null, 2);
    }
  })
  .catch(err => {
    const displayEl = document.getElementById("benchmark-data");
    if (displayEl) {
      displayEl.textContent = "❌ Failed to load benchmark data.\n\n" + err;
    }
  });
