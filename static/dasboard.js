if (typeof labels !== "undefined" && typeof importance !== "undefined") {

const importanceCanvas = document.getElementById("importanceChart");

if (importanceCanvas) {

new Chart(importanceCanvas, {

type: "bar",

data: {

labels: labels,

datasets: [{

label: "Feature Impact on Yield",

data: importance,

backgroundColor: [
"#16a34a",
"#22c55e",
"#4ade80",
"#86efac",
"#bbf7d0"
],

borderRadius: 6

}]

},

options: {

responsive: true,

plugins: {

legend: {
display: false
},

title: {
display: true,
text: "Feature Importance Analysis"
}

},

scales: {

y: {
beginAtZero: true
}

}

}

});

}

}



/*
   Temperature vs Yield Chart
 */

if (typeof temps !== "undefined" && typeof yields !== "undefined") {

const tempCanvas = document.getElementById("tempChart");

if (tempCanvas) {

new Chart(tempCanvas, {

type: "line",

data: {

labels: temps,

datasets: [{

label: "Predicted Yield",

data: yields,

fill: false,

borderColor: "#16a34a",

backgroundColor: "#16a34a",

tension: 0.3,

pointRadius: 4

}]

},

options: {

responsive: true,

plugins: {

title: {
display: true,
text: "Temperature vs Predicted Yield"
}

},

scales: {

x: {
title: {
display: true,
text: "Temperature (°C)"
}
},

y: {
title: {
display: true,
text: "Yield (tons/hectare)"
},
beginAtZero: true
}

}

}

});

}

}