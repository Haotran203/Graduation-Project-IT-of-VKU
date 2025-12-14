import React from "react";

const roles = {
  traveler: "Trả lời thân thiện, dễ áp dụng thực tế (du lịch, giờ mở cửa, chi phí)",
  student: "Giải thích súc tích, dễ hiểu để học tập",
  researcher: "Dẫn chứng chính xác, có trích dẫn nguồn thông tin",
  enthusiast: "Tường thuật sinh động, gợi cảm xúc, gắn yếu tố lịch sử - văn hóa",
};

export default function RoleSelect({ role, setRole }) {
  return (
    <div className="role-select">
      <label>Vai trò: </label>
      <select value={role} onChange={(e) => setRole(e.target.value)}>
        {Object.entries(roles).map(([key, desc]) => (
          <option key={key} value={key}>
            {key} – {desc}
          </option>
        ))}
      </select>
    </div>
  );
}
