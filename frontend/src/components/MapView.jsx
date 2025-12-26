// frontend/src/components/MapView.jsx - COMPLETE FIX

import React, { useState, useEffect } from "react";
import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

// ✅ FIX: Use CDN URLs directly (more reliable)
const DEFAULT_ICON = new L.Icon({
  iconUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
  iconRetinaUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
  shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

const SELECTED_ICON = new L.Icon({
  iconUrl: "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-red.png",
  shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

const removeDuplicateCoordinates = (coordinates, threshold = 0.001) => {
  if (!coordinates || coordinates.length === 0) return [];

  const unique = [];
  const seen = new Set();

  for (const coord of coordinates) {
    if (!coord || coord.latitude === undefined || coord.longitude === undefined) continue;
    if (isNaN(coord.latitude) || isNaN(coord.longitude)) continue;

    const lat = Math.round(coord.latitude / threshold) * threshold;
    const lng = Math.round(coord.longitude / threshold) * threshold;
    const key = `${lat},${lng}`;

    if (!seen.has(key)) {
      seen.add(key);
      unique.push(coord);
    }
  }

  return unique;
};

function MapController({ coords, currentIdx }) {
  const map = useMap();

  useEffect(() => {
    if (!coords || coords.length === 0) return;

    const validCoords = coords.filter(
      (c) =>
        c &&
        c.latitude !== undefined &&
        c.longitude !== undefined &&
        !isNaN(c.latitude) &&
        !isNaN(c.longitude)
    );

    if (validCoords.length === 0) return;

    if (validCoords.length > 1) {
      const bounds = L.latLngBounds(
        validCoords.map((c) => [c.latitude, c.longitude])
      );
      map.fitBounds(bounds, { padding: [50, 50] });
    } else {
      map.setView([validCoords[0].latitude, validCoords[0].longitude], 13);
    }
  }, [coords, map]);

  useEffect(() => {
    if (!coords || coords.length === 0 || currentIdx === undefined) return;

    const validCoords = coords.filter(
      (c) =>
        c &&
        c.latitude !== undefined &&
        c.longitude !== undefined &&
        !isNaN(c.latitude) &&
        !isNaN(c.longitude)
    );

    if (validCoords[currentIdx]) {
      const coord = validCoords[currentIdx];
      map.setView([coord.latitude, coord.longitude], 13, { animate: true });
    }
  }, [currentIdx, coords, map]);

  return null;
}

export default function MapView({ coords, onClose }) {
  const [currentMarkerIdx, setCurrentMarkerIdx] = useState(0);
  const [validCoords, setValidCoords] = useState([]);
  const [isMinimized, setIsMinimized] = useState(false);

  useEffect(() => {
    if (!coords || coords.length === 0) {
      setValidCoords([]);
      return;
    }

    const filtered = removeDuplicateCoordinates(coords, 0.001);
    setValidCoords(filtered);
    setCurrentMarkerIdx(0);
  }, [coords]);

  if (!validCoords || validCoords.length === 0) {
    return (
      <div className="map-empty">
        <p>📍 Không có tọa độ để hiển thị</p>
      </div>
    );
  }

  const center = [
    validCoords.reduce((sum, c) => sum + c.latitude, 0) / validCoords.length,
    validCoords.reduce((sum, c) => sum + c.longitude, 0) / validCoords.length,
  ];

  const handlePrevious = () => {
    setCurrentMarkerIdx(
      (prev) => (prev - 1 + validCoords.length) % validCoords.length
    );
  };

  const handleNext = () => {
    setCurrentMarkerIdx((prev) => (prev + 1) % validCoords.length);
  };

  if (isMinimized) {
    return (
      <div className="map-minimized">
        <button
          className="btn-restore-map"
          onClick={() => setIsMinimized(false)}
          title="Mở bản đồ"
        >
          🗺️ Bản đồ ({validCoords.length} địa điểm)
        </button>
      </div>
    );
  }

  return (
    <div className="map-view">
      <div className="map-header">
        <h3>📍 {validCoords.length} địa điểm</h3>
        <div className="map-header-actions">
          <button
            className="btn-minimize-map"
            onClick={() => setIsMinimized(true)}
            title="Thu gọn bản đồ"
          >
            −
          </button>
          <button
            className="btn-close-map"
            onClick={onClose}
            title="Đóng bản đồ"
          >
            ✕
          </button>
        </div>
      </div>

      <MapContainer
        center={center}
        zoom={validCoords.length === 1 ? 13 : 10}
        className="map-container"
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {validCoords.map((coord, idx) => (
          <Marker
            key={`${coord.latitude}-${coord.longitude}-${idx}`}
            position={[coord.latitude, coord.longitude]}
            title={coord.name || `Địa điểm ${idx + 1}`}
            icon={currentMarkerIdx === idx ? SELECTED_ICON : DEFAULT_ICON}
            eventHandlers={{
              click: () => setCurrentMarkerIdx(idx),
            }}
          >
            <Popup>
              <div style={{ fontFamily: "Arial", fontSize: "12px", minWidth: "150px" }}>
                <strong>{coord.name || `Địa điểm ${idx + 1}`}</strong>
                <br />
                📍 Vĩ độ: {coord.latitude.toFixed(4)}
                <br />
                📍 Kinh độ: {coord.longitude.toFixed(4)}
              </div>
            </Popup>
          </Marker>
        ))}

        <MapController coords={validCoords} currentIdx={currentMarkerIdx} />
      </MapContainer>

      <div className="map-controls">
        {validCoords.length > 1 && (
          <button
            className="btn-nav btn-prev"
            onClick={handlePrevious}
            title="Địa điểm trước"
          >
            ◀ Trước
          </button>
        )}

        <div className="map-legend-wrapper">
          <div className="map-legend">
            {validCoords.map((coord, idx) => (
              <div
                key={`${coord.latitude}-${coord.longitude}-legend-${idx}`}
                className={`legend-item ${
                  currentMarkerIdx === idx ? "active" : ""
                }`}
                onClick={() => setCurrentMarkerIdx(idx)}
                role="button"
                tabIndex={0}
                onKeyDown={(e) => {
                  if (e.key === "Enter") setCurrentMarkerIdx(idx);
                }}
              >
                <span className="legend-marker">📍</span>
                <span className="legend-text">
                  {idx + 1}. {coord.name || `Địa điểm ${idx + 1}`}
                </span>
              </div>
            ))}
          </div>
        </div>

        {validCoords.length > 1 && (
          <button
            className="btn-nav btn-next"
            onClick={handleNext}
            title="Địa điểm tiếp theo"
          >
            Tiếp ▶
          </button>
        )}
      </div>
    </div>
  );
}
