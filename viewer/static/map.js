# JavaScript
/**
 * @license
 * Copyright 2019 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */
// This example creates a simple polygon representing the Bermuda Triangle.
function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 5,
    center: { lat: 45.64656770181515, lng: 25.61757142545083 },
    mapTypeId: "terrain",
  });
  // Define the LatLng coordinates for the polygon's path.
  const polygonCoords = [
    { lat: 45.63669181834008, lng: 25.62158015131884 },
    { lat: 45.63987445923134, lng: 25.627789718512176 },
    { lat: 45.639120284194036, lng: 25.6285689920664 },
    { lat: 45.638217203132804, lng: 25.626241719512983 },
	{ lat: 45.638078690227154, lng: 25.625930462534942 },
	{ lat: 45.63622568281328, lng: 25.625803585438057 },
   { lat: 45.63517580696557, lng: 25.62384280447033 }

  ];
  // Construct the polygon.
  const agentBerzei = new google.maps.Polygon({
    paths: polygonCoords,
    strokeColor: "#6461bf",
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: "#FF0000",
    fillOpacity: 0.35,
  });

  agentBerzei.setMap(map);
}

window.initMap = initMap;