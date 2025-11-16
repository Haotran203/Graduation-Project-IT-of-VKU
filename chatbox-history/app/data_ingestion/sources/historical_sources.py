# app/data_ingestion/sources/historical_sources.py

# ==============================================================================
# SEED_HISTORICAL_ARTICLES
# Danh sách các bài viết CỰC KỲ QUAN TRỌNG hoặc có thể bị bỏ sót.
# Chúng được ưu tiên xử lý trước để đảm bảo kho kiến thức có nền tảng vững chắc.
# ==============================================================================
SEED_HISTORICAL_ARTICLES = [
    # --- Di sản UNESCO (Vật thể & Phi vật thể) ---
    "Vịnh Hạ Long", "Hoàng thành Huế", "Phố cổ Hội An", "Khu đền tháp Mỹ Sơn",
    "Thành nhà Hồ", "Vườn quốc gia Phong Nha-Kẻ Bàng", "Quần thể danh thắng Tràng An",
    "Cao nguyên đá Đồng Văn", "Nhã nhạc cung đình Huế", "Không gian văn hóa Cồng chiêng Tây Nguyên",
    "Ca trù", "Hát xoan", "Tín ngưỡng thờ cúng Hùng Vương", "Đờn ca tài tử Nam Bộ",
    "Nghi lễ và trò chơi kéo co", "Thực hành Tín ngưỡng thờ Mẫu Tam phủ của người Việt",
    "Nghệ thuật Bài chòi Trung Bộ Việt Nam", "Nghệ thuật Xòe Thái",

    # --- Nhân vật Lịch sử Tiêu biểu qua các thời kỳ ---
    "Hùng Vương", "An Dương Vương", "Hai Bà Trưng", "Bà Triệu", "Lý Nam Đế",
    "Triệu Quang Phục", "Ngô Quyền", "Đinh Tiên Hoàng", "Lê Đại Hành", "Lý Thái Tổ",
    "Lý Thường Kiệt", "Trần Nhân Tông", "Trần Hưng Đạo", "Chu Văn An", "Lê Lợi",
    "Nguyễn Trãi", "Lê Thánh Tông", "Nguyễn Bỉnh Khiêm", "Quang Trung", "Gia Long",
    "Minh Mạng", "Phan Bội Châu", "Phan Châu Trinh", "Hồ Chí Minh", "Võ Nguyên Giáp",

    # --- Sự kiện & Giai đoạn Lịch sử Trọng yếu ---
    "Thời kỳ Hồng Bàng", "Văn Lang", "Âu Lạc", "Bắc thuộc", "Chiến tranh Đông Dương",
    "Chiến tranh Việt Nam", "Trận Bạch Đằng (938)", "Chiến thắng Như Nguyệt", "Hội nghị Diên Hồng",
    "Khởi nghĩa Lam Sơn", "Phong trào Cần Vương", "Cách mạng tháng Tám", "Chiến dịch Điện Biên Phủ",
    "Hiệp định Genève, 1954", "Sự kiện Tết Mậu Thân", "Hiệp định Paris 1973",
    "Chiến dịch Hồ Chí Minh", "Ngày thống nhất", "Chiến tranh biên giới Việt–Trung 1979", "Đổi Mới",

    # --- Địa danh & Công trình Lịch sử - Văn hóa Nổi tiếng ---
    "Văn Miếu – Quốc Tử Giám", "Cố đô Hoa Lư", "Kinh thành Thăng Long", "Cổ Loa",
    "Địa đạo Củ Chi", "Dinh Độc Lập", "Hồ Gươm", "Sông Bạch Đằng",

    # --- Khái niệm Văn hóa & Xã hội Cốt lõi ---
    "Tết Nguyên Đán", "Tết Trung thu", "Giỗ Tổ Hùng Vương", "Nam quốc sơn hà", "Bình Ngô đại cáo",
]

# ==============================================================================
# HISTORICAL_SOURCES
# Danh sách các DANH MỤC trên Wikipedia để crawler tự động khám phá.
# Đây là phiên bản siêu mở rộng gấp 5 lần với hàng nghìn danh mục chi tiết.
# ==============================================================================
HISTORICAL_SOURCES = {
    "wikipedia_vi": {
        "categories": [
            # ==================== LỊCH SỬ (HISTORY) ====================
            # --- Lõi & Tổng quan ---
            "Lịch sử Việt Nam", "Biên niên sử Việt Nam", "Sử học Việt Nam", "Khảo cổ học Việt Nam",
            "Huyền sử Việt Nam", "Sự kiện lịch sử Việt Nam", "Nhân vật lịch sử Việt Nam",
            "Di sản thế giới tại Việt Nam", "Di tích quốc gia đặc biệt", "Di tích lịch sử Việt Nam",
            "Bảo tàng tại Việt Nam",
            "Lịch sử Việt Nam theo thời kỳ", "Lịch sử Việt Nam theo thế kỷ", "Lịch sử Việt Nam thế kỷ 20",
            "Lịch sử Việt Nam thế kỷ 19", "Lịch sử Việt Nam thế kỷ 18", "Lịch sử Việt Nam thế kỷ 17",
            "Lịch sử Việt Nam thế kỷ 16", "Lịch sử Việt Nam thế kỷ 15", "Lịch sử Việt Nam thế kỷ 14",
            "Lịch sử Việt Nam thế kỷ 13", "Lịch sử Việt Nam thế kỷ 12", "Lịch sử Việt Nam thế kỷ 11",
            "Lịch sử Việt Nam thế kỷ 10", "Lịch sử Việt Nam trước thế kỷ 10",

            # --- Các Triều đại & Giai đoạn (chi tiết) ---
            "Thời kỳ đồ đá tại Việt Nam", "Thời kỳ đồ đồng Việt Nam", "Văn hóa tiền sử Việt Nam",
            "Thời kỳ Hồng Bàng", "Văn Lang", "Âu Lạc", "Nam Việt",
            "Bắc thuộc", "Giao Chỉ", "An Nam đô hộ phủ", "Tĩnh Hải quân",
            "Bắc thuộc lần 1", "Bắc thuộc lần 2", "Bắc thuộc lần 3", "Bắc thuộc lần 4",
            "Thời kỳ tự chủ Việt Nam", "Họ Khúc", "Họ Dương", "Nhà Ngô", "Loạn 12 sứ quân", "Nhà Đinh",
            "Nhà Tiền Lê", "Nhà Lý", "Nhà Trần", "Nhà Hồ", "Nhà Hậu Trần", "Nhà Hậu Lê", "Nhà Mạc",
            "Trịnh-Nguyễn phân tranh", "Chúa Trịnh", "Chúa Nguyễn", "Đàng Trong", "Đàng Ngoài",
            "Nhà Tây Sơn", "Nhà Nguyễn", "Lịch sử Việt Nam thời Pháp thuộc", "Liên bang Đông Dương",
            "Việt Nam Dân chủ Cộng hòa", "Quốc gia Việt Nam", "Việt Nam Cộng hòa",
            "Cộng hòa Xã hội chủ nghĩa Việt Nam", "Lịch sử Việt Nam (1945–1975)", "Lịch sử Việt Nam sau 1975",
            "Lịch sử Việt Nam 1975-1986", "Lịch sử Việt Nam sau 1986", "Thời kỳ đổi mới",
            "Vua Lý", "Vua Trần", "Vua Lê", "Vua Nguyễn", "Hoàng tử Việt Nam", "Công chúa Việt Nam",

            # --- Chiến tranh & Quân sự (chi tiết) ---
            "Chiến tranh tại Việt Nam", "Các trận đánh trong lịch sử Việt Nam", "Quân sự Việt Nam",
            "Lịch sử quân sự Việt Nam", "Tướng lĩnh Việt Nam", "Vũ khí Việt Nam", "Trang bị Quân đội Nhân dân Việt Nam",
            "Chiến tranh Tống-Việt", "Kháng chiến chống quân Mông-Nguyên", "Chiến tranh Minh-Đại Ngu",
            "Chiến tranh Đại Việt-Chiêm Thành", "Chiến tranh Đại Việt-Lan Xang", "Chiến tranh Xiêm-Việt",
            "Chiến tranh Pháp-Thanh", "Kháng chiến chống Pháp", "Kháng chiến chống Mỹ",
            "Các chiến dịch trong Chiến tranh Việt Nam",
            "Quân đội Nhân dân Việt Nam", "Quân lực Việt Nam Cộng hòa", "Hải quân Nhân dân Việt Nam",
            "Không quân Nhân dân Việt Nam",
            "Bộ đội Biên phòng Việt Nam", "Công an nhân dân Việt Nam", "Dân quân tự vệ Việt Nam",
            "Các trận đánh thời Lý", "Các trận đánh thời Trần", "Các trận đánh thời Lê",
            "Trận Bạch Đằng", "Trận Chi Lăng", "Trận Tốt Động - Chúc Động", "Trận Rạch Gầm-Xoài Mút",
            "Chiến dịch Biên giới 1950", "Chiến dịch Hòa Bình", "Chiến dịch Tây Bắc", "Chiến dịch Điện Biên Phủ",
            "Chiến dịch Hồ Chí Minh", "Chiến dịch Tết Mậu Thân", "Chiến dịch đường 9 - Nam Lào",
            "Trận Vị Xuyên", "Trận Hà Nội", "Trận Điện Biên Phủ trên không",
            "Anh hùng Lực lượng vũ trang nhân dân Việt Nam", "Liệt sĩ Việt Nam", "Nghĩa trang liệt sĩ",
            "Huân chương Quân đội nhân dân Việt Nam", "Huy chương Quân đội nhân dân Việt Nam",

            # --- Chính trị, Luật pháp & Hiệp ước (chi tiết) ---
            "Vua Việt Nam", "Hoàng hậu Việt Nam", "Thái hậu Việt Nam", "Thái giám trong lịch sử Việt Nam",
            "Quan lại Việt Nam", "Chính trị Việt Nam", "Lịch sử hành chính Việt Nam",
            "Các đơn vị hành chính cũ của Việt Nam",
            "Ngoại giao Việt Nam", "Quan hệ ngoại giao của Việt Nam", "Hiệp ước trong lịch sử Việt Nam",
            "Hội nghị trong lịch sử Việt Nam",
            "Tên gọi Việt Nam qua các thời kỳ", "Quốc hiệu Việt Nam", "Quốc kỳ Việt Nam", "Quốc huy Việt Nam",
            "Thủ đô Việt Nam qua các thời kỳ", "Luật pháp Việt Nam thời phong kiến", "Khoa cử Việt Nam",
            "Trạng nguyên Việt Nam",
            "Đảng Cộng sản Việt Nam", "Mặt trận Tổ quốc Việt Nam", "Quốc hội Việt Nam", "Chính phủ Việt Nam",
            "Chủ tịch nước Việt Nam", "Thủ tướng Chính phủ Việt Nam", "Chủ tịch Quốc hội Việt Nam",
            "Tổng Bí thư Ban Chấp hành Trung ương Đảng Cộng sản Việt Nam",
            "Hiến pháp Việt Nam", "Luật Việt Nam", "Hệ thống pháp luật Việt Nam", "Tòa án Việt Nam",
            "Viện kiểm sát Việt Nam", "Bộ máy nhà nước Việt Nam", "Các bộ của Việt Nam",
            "Cải cách hành chính tại Việt Nam", "Cải cách tư pháp tại Việt Nam",

            # --- Khởi nghĩa & Phong trào Cách mạng ---
            "Khởi nghĩa tại Việt Nam", "Khởi nghĩa Hai Bà Trưng", "Khởi nghĩa Bà Triệu", "Khởi nghĩa Lý Bí",
            "Khởi nghĩa Mai Thúc Loan", "Khởi nghĩa Phùng Hưng", "Khởi nghĩa Lam Sơn", "Khởi nghĩa Tây Sơn",
            "Phong trào Cần Vương", "Phong trào Đông Du", "Phong trào Duy Tân", "Phong trào Văn Thân",
            "Việt Nam Quốc Dân Đảng", "Việt Nam Quang Phục Hội", "Phong trào cộng sản Việt Nam",
            "Cách mạng tháng Tám", "Tổng khởi nghĩa tháng Tám", "Ngày Quốc khánh Việt Nam",

            # --- Nhân vật Lịch sử (mở rộng) ---
            "Danh nhân Việt Nam", "Anh hùng dân tộc Việt Nam", "Danh tướng Việt Nam", "Văn thần Việt Nam",
            "Nhà nho Việt Nam", "Nhà thơ Việt Nam thời phong kiến", "Nữ anh hùng Việt Nam",
            "Nhà cách mạng Việt Nam", "Nhà hoạt động chính trị Việt Nam", "Nhà ngoại giao Việt Nam",
            "Thái giám Việt Nam", "Nghệ nhân Việt Nam", "Thương nhân Việt Nam trong lịch sử",

            # ==================== VĂN HÓA & XÃ HỘI (CULTURE & SOCIETY) ====================
            # --- Tổng quan & Phong tục ---
            "Văn hóa Việt Nam", "Văn hóa Đông Sơn", "Văn hóa Sa Huỳnh", "Văn hóa Óc Eo",
            "Văn hóa Hoà Bình", "Văn hóa Bắc Sơn", "Văn hóa Phùng Nguyên", "Văn hóa Đồng Đậu",
            "Phong tục Việt Nam", "Hôn nhân Việt Nam", "Tang lễ Việt Nam", "Làng xã Việt Nam", "Hương ước",
            "Tín ngưỡng dân gian Việt Nam", "Thần thoại Việt Nam", "Truyền thuyết Việt Nam", "Cổ tích Việt Nam",
            "Lễ hội Việt Nam", "Tết", "Tết Nguyên Đán", "Tết Đoan Ngọ", "Tết Trung thu", "Tết Hàn thực",
            "Lễ hội truyền thống Việt Nam", "Lễ hội dân gian Việt Nam", "Lễ hội miền Bắc", "Lễ hội miền Trung",
            "Lễ hội miền Nam",
            "Trang phục Việt Nam", "Áo dài", "Áo tứ thân", "Áo bà ba", "Nón lá", "Khăn đóng",
            "Trang phục cổ Việt Nam", "Trang phục cung đình Việt Nam", "Trang phục dân tộc Việt Nam",
            "Đạo đức Việt Nam", "Giá trị truyền thống Việt Nam", "Lễ nghi Việt Nam", "Tục lệ Việt Nam",
            "Gia đình Việt Nam", "Dòng họ Việt Nam", "Gia phả Việt Nam", "Làng quê Việt Nam",
            "Văn hóa làng xã Việt Nam", "Cộng đồng người Việt", "Cộng đồng người Việt ở nước ngoài",
            "Người Việt Nam", "Bản sắc văn hóa Việt Nam", "Di sản văn hóa Việt Nam",

            # --- Tôn giáo & Tín ngưỡng (chi tiết) ---
            "Tôn giáo tại Việt Nam", "Phật giáo Việt Nam", "Lịch sử Phật giáo Việt Nam", "Thiền phái Trúc Lâm",
            "Chùa Việt Nam",
            "Thiền phái Việt Nam", "Phật giáo Bắc truyền tại Việt Nam", "Phật giáo Nam truyền tại Việt Nam",
            "Tăng ni Phật giáo Việt Nam", "Hòa thượng Việt Nam", "Thiền sư Việt Nam", "Chùa tại Hà Nội",
            "Chùa tại Thành phố Hồ Chí Minh", "Chùa tại Huế", "Tháp Việt Nam", "Tượng Phật Việt Nam",
            "Công giáo tại Việt Nam", "Lịch sử Công giáo tại Việt Nam", "Nhà thờ tại Việt Nam",
            "Giáo phận Công giáo tại Việt Nam",
            "Giám mục Công giáo Việt Nam", "Linh mục Việt Nam", "Tu sĩ Công giáo Việt Nam",
            "Nhà thờ tại Hà Nội", "Nhà thờ tại Thành phố Hồ Chí Minh", "Thánh đường Công giáo Việt Nam",
            "Tin Lành tại Việt Nam", "Hồi giáo tại Việt Nam", "Cao Đài", "Hòa Hảo", "Bửu Sơn Kỳ Hương",
            "Tứ bất tử", "Thờ Mẫu", "Tín ngưỡng thờ cúng tổ tiên", "Đạo giáo tại Việt Nam", "Nho giáo tại Việt Nam",
            "Thờ cúng Việt Nam", "Đền thờ Việt Nam", "Miếu thờ Việt Nam", "Nghĩa trang Việt Nam",
            "Thánh thần Việt Nam", "Thành hoàng làng", "Thần linh Việt Nam", "Thánh mẫu", "Linh sơn thánh mẫu",
            "Đạo Mẫu", "Hầu đồng", "Lên đồng", "Tục thờ cúng Việt Nam",

            # --- Ẩm thực (chi tiết) ---
            "Ẩm thực Việt Nam", "Ẩm thực cung đình Huế", "Ẩm thực miền Bắc, Việt Nam", "Ẩm thực miền Trung, Việt Nam",
            "Ẩm thực miền Nam, Việt Nam",
            "Các món ăn Việt Nam", "Các món phở", "Các món bún", "Các món bánh Việt Nam", "Các món chè", "Các món lẩu",
            "Phở", "Bánh mì Việt Nam", "Nem rán", "Bún chả", "Gỏi cuốn", "Bánh xèo", "Bún bò Huế", "Hủ tiếu",
            "Cơm tấm", "Bánh cuốn", "Bánh bèo", "Bánh bột lọc", "Bánh ít", "Bánh tét", "Bánh chưng",
            "Bún riêu", "Bún thang", "Bún ốc", "Bún mắm", "Bún đậu mắm tôm", "Miến lươn", "Miến gà",
            "Cao lầu", "Mì Quảng", "Bánh canh", "Hủ tiếu Nam Vang", "Hủ tiếu Mỹ Tho",
            "Chả cá", "Chả lụa", "Giò lụa", "Giò thủ", "Nem chua", "Thịt kho", "Cá kho",
            "Canh chua", "Lẩu Thái", "Lẩu mắm", "Lẩu cá", "Gỏi Việt Nam", "Gỏi gà", "Gỏi ngó sen",
            "Chè Việt Nam", "Chè ba màu", "Chè bưởi", "Chè đậu xanh", "Chè thái",
            "Bánh trung thu", "Bánh dày", "Bánh giầy", "Bánh phu thê", "Bánh đúc", "Bánh khọt",
            "Nước mắm", "Gia vị Việt Nam", "Rau thơm Việt Nam", "Đồ uống Việt Nam", "Văn hóa ẩm thực Việt Nam",
            "Trà Việt Nam", "Văn hóa cà phê Việt Nam", "Rượu Việt Nam", "Rượu nếp", "Rượu cần",
            "Ẩm thực đường phố Việt Nam", "Chợ Việt Nam", "Quán ăn Việt Nam", "Nhà hàng Việt Nam",
            "Nghề làm bánh Việt Nam", "Nghề làm nước mắm", "Nghề làm chả", "Bếp Việt Nam",

            # --- Ngôn ngữ & Dân tộc (chi tiết) ---
            "Ngôn ngữ tại Việt Nam", "Tiếng Việt", "Lịch sử tiếng Việt", "Chữ Nôm", "Chữ Quốc ngữ",
            "Chữ Hán Việt Nam", "Chữ viết Việt Nam", "Ngữ pháp tiếng Việt", "Từ vựng tiếng Việt",
            "Phương ngữ tiếng Việt", "Tiếng Việt miền Bắc", "Tiếng Việt miền Trung", "Tiếng Việt miền Nam",
            "Giọng Hà Nội", "Giọng Huế", "Giọng Sài Gòn", "Thành ngữ Việt Nam", "Ca dao Việt Nam", "Tục ngữ Việt Nam",
            "Các dân tộc tại Việt Nam", "Người Kinh", "Người Hoa tại Việt Nam", "Người Chăm",
            "Người Khmer tại Việt Nam",
            "Các dân tộc thiểu số ở Việt Nam", "Trang phục các dân tộc Việt Nam",
            "Người Tày", "Người Thái", "Người Mường", "Người Nùng", "Người H'Mông", "Người Dao",
            "Người Gia Rai", "Người Ê Đê", "Người Ba Na", "Người Xơ Đăng", "Người Sán Chay", "Người Cơ Ho",
            "Người Chăm", "Người Sán Dìu", "Người Hrê", "Người Mnông", "Người Ra Glai", "Người Xtiêng",
            "Người Bru-Vân Kiều", "Người Thổ", "Người Giáy", "Người Cơ Tu", "Người Gié Triêng", "Người Mạ",
            "Người Khơ Mú", "Người Co", "Người Tà Ôi", "Người Chơ Ro", "Người Kháng", "Người Xinh Mun",
            "Người Hà Nhì", "Người Chu Ru", "Người Lào", "Người La Chí", "Người La Ha", "Người Phù Lá",
            "Người La Hủ", "Người Lự", "Người Lô Lô", "Người Chứt", "Người Mảng", "Người Pà Thẻn",
            "Người Cơ Lao", "Người Cống", "Người Bố Y", "Người Si La", "Người Pu Péo", "Người Brâu",
            "Người Ơ Đu", "Người Rơ Măm",

            # ==================== NGHỆ THUẬT (ARTS) ====================
            # --- Tổng quan & Kiến trúc ---
            "Nghệ thuật Việt Nam", "Mỹ thuật Việt Nam", "Kiến trúc Việt Nam", "Kiến trúc cổ Việt Nam",
            "Kiến trúc cung đình Huế", "Kiến trúc Pháp thuộc tại Việt Nam", "Nhà rông", "Đình làng", "Chùa Việt Nam",
            "Kiến trúc dân gian Việt Nam", "Kiến trúc nhà ở Việt Nam", "Nhà sàn", "Nhà tranh",
            "Kiến trúc tôn giáo Việt Nam", "Kiến trúc phố cổ Việt Nam", "Kiến trúc đô thị Việt Nam",
            "Công trình kiến trúc Việt Nam", "Cổng làng Việt Nam", "Cầu Việt Nam", "Cầu ngói",
            "Lăng tẩm Việt Nam", "Lăng vua Việt Nam", "Lăng Chủ tịch Hồ Chí Minh",
            "Nhà thờ họ Việt Nam", "Từ đường Việt Nam", "Dinh thự Việt Nam",

            # --- Âm nhạc (chi tiết) ---
            "Âm nhạc Việt Nam", "Lịch sử âm nhạc Việt Nam", "Nhạc cổ truyền Việt Nam", "Dân ca Việt Nam",
            "Nhã nhạc cung đình Huế", "Ca trù",
            "Quan họ", "Hát chèo", "Hát tuồng", "Hát xẩm", "Cải lương", "Đờn ca tài tử Nam Bộ",
            "Nhạc tiền chiến", "Nhạc đỏ", "Nhạc vàng", "Nhạc trẻ Việt Nam", "V-pop", "Nhạc rock Việt Nam",
            "Nhạc sĩ Việt Nam", "Ca sĩ Việt Nam", "Ban nhạc Việt Nam", "Nhạc cụ cổ truyền Việt Nam",
            "Hát dân ca Việt Nam", "Hò Việt Nam", "Lý Việt Nam", "Hát ru Việt Nam", "Hát múa dân gian",
            "Hát then", "Hát soóng cô", "Hát ví", "Hát giặm", "Hát đúm", "Hát khăn", "Hò khoan",
            "Hát bội", "Hát ả đào", "Hát văn", "Hát xoan Phú Thọ", "Hát bài chòi", "Hát xẩm",
            "Đàn bầu", "Đàn tranh", "Đàn nguyệt", "Đàn tỳ bà", "Đàn nhị", "Đàn tam", "Đàn cò",
            "Sáo trúc", "Kèn bầu", "Kèn lá", "Trống", "Cồng chiêng", "Sến", "T'rưng",
            "Nhạc lễ Việt Nam", "Nhạc cung đình", "Nhạc Phật giáo Việt Nam", "Nhạc lễ hội",
            "Nhạc Bolero Việt Nam", "Nhạc Pop Việt Nam", "Nhạc Hip hop Việt Nam", "Nhạc EDM Việt Nam",
            "Nhạc indie Việt Nam", "Nhạc ballad Việt Nam", "Nhạc Dance Việt Nam",
            "Giải thưởng âm nhạc Việt Nam", "Album nhạc Việt Nam", "Single Việt Nam",
            "Nhà sản xuất âm nhạc Việt Nam", "Công ty giải trí Việt Nam", "Festival âm nhạc Việt Nam",

            # --- Sân khấu, Hội họa, Điêu khắc (chi tiết) ---
            "Sân khấu Việt Nam", "Múa rối nước Việt Nam", "Hội họa Việt Nam", "Họa sĩ Việt Nam",
            "Tranh Đông Hồ", "Tranh Hàng Trống", "Hội họa sơn mài", "Tranh lụa",
            "Điêu khắc Việt Nam", "Điêu khắc Chăm Pa", "Điêu khắc gỗ đình làng", "Gốm Việt Nam", "Gốm Chu Đậu",
            "Gốm Bát Tràng",
            "Kịch nói Việt Nam", "Kịch câm Việt Nam", "Nhà hát kịch", "Đạo diễn sân khấu Việt Nam",
            "Diễn viên sân khấu Việt Nam", "Múa Việt Nam", "Múa dân gian Việt Nam", "Múa cổ điển Việt Nam",
            "Múa đương đại Việt Nam", "Biên đạo múa Việt Nam", "Nghệ sĩ múa Việt Nam",
            "Tranh dân gian Việt Nam", "Tranh sơn dầu Việt Nam", "Tranh thuỷ mặc Việt Nam",
            "Mỹ thuật hiện đại Việt Nam", "Mỹ thuật đương đại Việt Nam", "Mỹ thuật ứng dụng Việt Nam",
            "Thiết kế đồ họa Việt Nam", "Nhiếp ảnh Việt Nam", "Nhiếp ảnh gia Việt Nam",
            "Điêu khắc đá Việt Nam", "Điêu khắc đồng Việt Nam", "Điêu khắc gỗ Việt Nam",
            "Tượng đài Việt Nam", "Phù điêu Việt Nam", "Nghề chạm khắc Việt Nam",
            "Gốm sứ Việt Nam", "Gốm Đông Triều", "Gốm Biên Hòa", "Gốm Thanh Hà", "Gốm Phù Lãng",
            "Sơn mài Việt Nam", "Tranh sơn mài Việt Nam", "Nghề sơn mài", "Khảm trai",
            "Thêu Việt Nam", "Thêu tay Việt Nam", "Tơ lụa Việt Nam", "Nghề dệt Việt Nam",
            "Mây tre đan Việt Nam", "Mộc mỹ nghệ", "Đồ gỗ mỹ nghệ", "Sừng trâu",
            "Tranh sơn ta", "Thư pháp Việt Nam", "Hán Nôm thư pháp",

            # --- Văn học & Điện ảnh (chi tiết) ---
            "Văn học Việt Nam", "Văn học dân gian Việt Nam", "Văn học trung đại Việt Nam", "Văn học hiện đại Việt Nam",
            "Thơ mới (phong trào)", "Tự Lực văn đoàn", "Nhà văn Việt Nam", "Nhà thơ Việt Nam", "Truyện Kiều",
            "Điện ảnh Việt Nam", "Lịch sử điện ảnh Việt Nam", "Phim kinh điển Việt Nam", "Đạo diễn Việt Nam",
            "Diễn viên Việt Nam",
            "Liên hoan phim Việt Nam", "Giải Cánh diều",
            "Thơ Việt Nam", "Thơ Nôm", "Thơ chữ Hán", "Thơ Quốc ngữ", "Thơ ca cổ điển Việt Nam",
            "Thơ lục bát", "Thơ song thất lục bát", "Thơ tứ tuyệt", "Thơ Đường luật",
            "Truyện thơ Nôm", "Truyện thơ Việt Nam", "Lục Vân Tiên", "Phan Trần", "Hoa Tiên",
            "Truyện ngắn Việt Nam", "Tiểu thuyết Việt Nam", "Truyện dài Việt Nam", "Văn xuôi Việt Nam",
            "Tản văn Việt Nam", "Kí Việt Nam", "Hồi ký Việt Nam", "Nhật ký Việt Nam",
            "Văn học cách mạng Việt Nam", "Văn học kháng chiến", "Thơ kháng chiến",
            "Văn học đương đại Việt Nam", "Văn học trẻ Việt Nam", "Tiểu thuyết lịch sử Việt Nam",
            "Truyện trinh thám Việt Nam", "Truyện kiếm hiệp Việt Nam", "Văn học thiếu nhi Việt Nam",
            "Giải thưởng văn học Việt Nam", "Giải thưởng Hồ Chí Minh", "Giải thưởng Nhà nước",
            "Nhà xuất bản Việt Nam", "Tạp chí văn học Việt Nam", "Báo văn học nghệ thuật",
            "Phê bình văn học Việt Nam", "Nghiên cứu văn học Việt Nam", "Lý luận văn học Việt Nam",
            "Phim truyện Việt Nam", "Phim tài liệu Việt Nam", "Phim hoạt hình Việt Nam",
            "Phim chiến tranh Việt Nam", "Phim tình cảm Việt Nam", "Phim hài Việt Nam",
            "Phim kinh dị Việt Nam", "Phim hành động Việt Nam", "Phim lịch sử Việt Nam",
            "Hãng phim Việt Nam", "Xưởng phim Việt Nam", "Rạp chiếu phim Việt Nam",
            "Giải thưởng điện ảnh Việt Nam", "Liên hoan phim quốc tế Việt Nam",
            "Kịch bản phim Việt Nam", "Quay phim Việt Nam", "Dựng phim Việt Nam",
            "Âm thanh phim Việt Nam", "Nhạc phim Việt Nam", "Diễn xuất điện ảnh Việt Nam",

            # ==================== ĐỊA LÝ & THIÊN NHIÊN (GEOGRAPHY & NATURE) ====================
            # --- Địa lý Hành chính & Tự nhiên (chi tiết) ---
            "Địa lý Việt Nam", "Phân cấp hành chính Việt Nam", "Các vùng của Việt Nam", "Tỉnh thành Việt Nam",
            "Thành phố trực thuộc trung ương (Việt Nam)", "Thành phố thuộc tỉnh (Việt Nam)",
            "Danh sách các huyện thị xã thành phố thuộc tỉnh của Việt Nam",
            "Sông ngòi Việt Nam", "Hệ thống sông Hồng", "Hệ thống sông Cửu Long", "Núi ở Việt Nam",
            "Dãy núi Trường Sơn", "Phan Xi Păng",
            "Đèo tại Việt Nam", "Đảo Việt Nam", "Quần đảo Hoàng Sa", "Quần đảo Trường Sa", "Phú Quốc", "Côn Đảo",
            "Lý Sơn",
            "Vịnh Việt Nam", "Hang động ở Việt Nam", "Hồ tại Việt Nam", "Cao nguyên Việt Nam", "Bán đảo Việt Nam",
            "Đồng bằng sông Cửu Long",
            "Đồng bằng sông Hồng", "Miền núi phía Bắc", "Bắc Trung Bộ", "Duyên hải Nam Trung Bộ", "Tây Nguyên",
            "Đông Nam Bộ", "Tây Nam Bộ", "Miền Bắc Việt Nam", "Miền Trung Việt Nam", "Miền Nam Việt Nam",
            "Quận ở Việt Nam", "Huyện ở Việt Nam", "Thị xã Việt Nam", "Xã Việt Nam", "Phường Việt Nam",
            "Thị trấn Việt Nam",
            "Địa danh Việt Nam", "Tên gọi địa phương Việt Nam", "Lịch sử địa danh Việt Nam",
            "Sông Hồng", "Sông Đà", "Sông Lô", "Sông Thao", "Sông Chảy", "Sông Gâm", "Sông Mã", "Sông Chu",
            "Sông Cả", "Sông Lam", "Sông Thu Bồn", "Sông Hương", "Sông Ba", "Sông Đồng Nai", "Sông Sài Gòn",
            "Sông Tiền", "Sông Hậu", "Sông Vàm Cỏ", "Kênh Đông", "Kênh Nhiêu Lộc - Thị Nghè",
            "Vịnh Hạ Long", "Vịnh Lan Hạ", "Vịnh Bái Tử Long", "Vịnh Vân Phong", "Vịnh Nha Trang",
            "Vịnh Cam Ranh", "Vịnh Xuân Đài", "Biển Đông", "Biển Việt Nam",
            "Đèo Hải Vân", "Đèo Ngang", "Đèo Cả", "Đèo Phượng Hoàng", "Đèo Ô Quy Hồ", "Đèo Khau Phạ",
            "Núi Ngũ Hành Sơn", "Núi Bà Đen", "Núi Chứa Chan", "Núi Tà Cu", "Núi Bà Rá", "Núi Sam",
            "Hang Sơn Đoòng", "Hang Én", "Động Phong Nha", "Động Thiên Đường", "Động Hương Tích",
            "Hồ Tây", "Hồ Hoàn Kiếm", "Hồ Ba Bể", "Hồ Núi Cốc", "Hồ Thác Bà", "Hồ Trị An", "Hồ Dầu Tiếng",
            "Cao nguyên Đồng Văn", "Cao nguyên Mộc Châu", "Cao nguyên Lâm Viên", "Cao nguyên Di Linh",

            # --- Môi trường & Sinh thái (chi tiết) ---
            "Vườn quốc gia Việt Nam", "Khu dự trữ sinh quyển Việt Nam", "Khu bảo tồn thiên nhiên Việt Nam",
            "Động vật Việt Nam", "Sách Đỏ Việt Nam", "Thực vật Việt Nam", "Khí hậu Việt Nam",
            "Vườn quốc gia Cúc Phương", "Vườn quốc gia Ba Vì", "Vườn quốc gia Tam Đảo", "Vườn quốc gia Xuân Sơn",
            "Vườn quốc gia Hoàng Liên", "Vườn quốc gia Ba Bể", "Vườn quốc gia Phong Nha-Kẻ Bàng",
            "Vườn quốc gia Bạch Mã", "Vườn quốc gia Bidoup - Núi Bà", "Vườn quốc gia Cát Tiên",
            "Vườn quốc gia Côn Đảo", "Vườn quốc gia Phú Quốc", "Vườn quốc gia U Minh Thượng",
            "Vườn quốc gia Tràm Chim", "Vườn quốc gia Mũi Cà Mau", "Vườn quốc gia Núi Chúa",
            "Khu dự trữ sinh quyển Cần Giờ", "Khu dự trữ sinh quyển đồng bằng sông Hồng",
            "Khu dự trữ sinh quyển Tây Nghệ An", "Khu dự trữ sinh quyển Cát Bà",
            "Động vật có vú Việt Nam", "Chim Việt Nam", "Bò sát Việt Nam", "Lưỡng cư Việt Nam",
            "Cá Việt Nam", "Côn trùng Việt Nam", "Động vật quý hiếm Việt Nam",
            "Hổ Đông Dương", "Tê giác Java", "Voi châu Á", "Voọc Việt Nam", "Sao la", "Mang lớn",
            "Gấu ngựa", "Hươu sao", "Rùa biển", "Cá sấu Xiêm", "Trăn gấm", "Kỳ đà",
            "Cây gỗ Việt Nam", "Cây dược liệu Việt Nam", "Cây ăn quả Việt Nam", "Hoa Việt Nam",
            "Rừng nhiệt đới Việt Nam", "Rừng ngập mặn Việt Nam", "Rừng trên núi đá vôi",
            "Khí hậu nhiệt đới gió mùa", "Mùa mưa Việt Nam", "Mùa khô Việt Nam", "Bão Việt Nam",
            "Lũ lụt Việt Nam", "Hạn hán Việt Nam", "Biến đổi khí hậu tại Việt Nam",
            "Môi trường Việt Nam", "Ô nhiễm môi trường Việt Nam", "Bảo vệ môi trường Việt Nam",

            # ==================== KINH TẾ & KHOA HỌC (ECONOMY & SCIENCE) ====================
            # --- Kinh tế (chi tiết) ---
            "Kinh tế Việt Nam", "Lịch sử kinh tế Việt Nam", "Đổi Mới", "Nông nghiệp Việt Nam", "Trồng lúa ở Việt Nam",
            "Làng nghề Việt Nam", "Công nghiệp Việt Nam", "Dịch vụ ở Việt Nam", "Du lịch Việt Nam",
            "Giao thông Việt Nam", "Đường sắt Việt Nam", "Hàng không Việt Nam", "Hệ thống đường bộ Việt Nam",
            "Ngân hàng tại Việt Nam", "Sàn giao dịch chứng khoán Thành phố Hồ Chí Minh",
            "Sàn giao dịch chứng khoán Hà Nội",
            "Kinh tế thị trường định hướng xã hội chủ nghĩa", "Kế hoạch 5 năm Việt Nam",
            "GDP Việt Nam", "Xuất khẩu Việt Nam", "Nhập khẩu Việt Nam", "Thương mại Việt Nam",
            "Đầu tư nước ngoài tại Việt Nam", "Khu công nghiệp Việt Nam", "Khu kinh tế Việt Nam",
            "Nông nghiệp và Phát triển nông thôn Việt Nam", "Trồng trọt Việt Nam", "Chăn nuôi Việt Nam",
            "Thuỷ sản Việt Nam", "Lâm nghiệp Việt Nam", "Cà phê Việt Nam", "Cao su Việt Nam",
            "Hạt điều Việt Nam", "Hồ tiêu Việt Nam", "Trà Việt Nam", "Gạo Việt Nam",
            "Chăn nuôi lợn", "Chăn nuôi gia cầm", "Nuôi trồng thuỷ sản", "Nuôi tôm", "Nuôi cá tra",
            "Công nghiệp chế biến Việt Nam", "Công nghiệp nặng Việt Nam", "Công nghiệp nhẹ Việt Nam",
            "Công nghiệp dệt may Việt Nam", "Công nghiệp giày da Việt Nam", "Công nghiệp điện tử Việt Nam",
            "Công nghiệp ô tô Việt Nam", "Công nghiệp thép Việt Nam", "Công nghiệp xi măng Việt Nam",
            "Năng lượng Việt Nam", "Điện lực Việt Nam", "Dầu khí Việt Nam", "Than đá Việt Nam",
            "Năng lượng tái tạo Việt Nam", "Điện mặt trời Việt Nam", "Điện gió Việt Nam", "Thuỷ điện Việt Nam",
            "Dịch vụ tài chính Việt Nam", "Ngân hàng thương mại Việt Nam", "Bảo hiểm Việt Nam",
            "Chứng khoán Việt Nam", "Bất động sản Việt Nam", "Bưu chính Việt Nam", "Viễn thông Việt Nam",
            "Du lịch văn hóa Việt Nam", "Du lịch sinh thái Việt Nam", "Du lịch biển đảo", "Du lịch miền núi",
            "Khách sạn Việt Nam", "Nhà hàng Việt Nam", "Resort Việt Nam", "Homestay Việt Nam",
            "Đường cao tốc Việt Nam", "Cầu đường Việt Nam", "Đường sắt đô thị", "Metro Hà Nội",
            "Metro Thành phố Hồ Chí Minh",
            "Sân bay quốc tế Nội Bài", "Sân bay quốc tế Tân Sơn Nhất", "Sân bay quốc tế Đà Nẵng",
            "Hãng hàng không Việt Nam", "Vietnam Airlines", "Vietjet Air", "Bamboo Airways",
            "Cảng biển Việt Nam", "Cảng Hải Phòng", "Cảng Sài Gòn", "Cảng Đà Nẵng", "Cảng Cái Mép",
            "Thương hiệu Việt Nam", "Công ty Việt Nam", "Tập đoàn kinh tế Việt Nam", "Doanh nghiệp nhà nước",
            "Doanh nghiệp tư nhân Việt Nam", "Start-up Việt Nam", "Công nghệ thông tin Việt Nam",

            # --- Khoa học & Giáo dục (chi tiết) ---
            "Khoa học và công nghệ tại Việt Nam", "Nhà khoa học Việt Nam", "Phát minh của người Việt",
            "Giáo dục tại Việt Nam", "Hệ thống giáo dục Việt Nam", "Trường Đại học và Viện nghiên cứu tại Việt Nam",
            "Viện Hàn lâm Khoa học và Công nghệ Việt Nam", "Viện Khoa học xã hội Việt Nam",
            "Bộ Khoa học và Công nghệ (Việt Nam)", "Bộ Giáo dục và Đào tạo (Việt Nam)",
            "Nghiên cứu khoa học Việt Nam", "Công nghệ sinh học Việt Nam", "Công nghệ thông tin Việt Nam",
            "Khoa học vật liệu Việt Nam", "Khoa học môi trường Việt Nam", "Y học Việt Nam",
            "Y học cổ truyền Việt Nam", "Thuốc Nam", "Đông y Việt Nam", "Bệnh viện Việt Nam",
            "Giáo dục mầm non Việt Nam", "Giáo dục phổ thông Việt Nam", "Giáo dục trung học Việt Nam",
            "Giáo dục đại học Việt Nam", "Giáo dục nghề nghiệp Việt Nam", "Giáo dục thường xuyên",
            "Đại học Quốc gia Hà Nội", "Đại học Quốc gia Thành phố Hồ Chí Minh",
            "Đại học Bách khoa Hà Nội", "Đại học Y Hà Nội", "Đại học Sư phạm Hà Nội",
            "Đại học Khoa học Tự nhiên", "Đại học Khoa học Xã hội và Nhân văn",
            "Học viện Quân y", "Học viện Chính trị quốc gia Hồ Chí Minh", "Học viện Ngoại giao",
            "Trường trung học phổ thông chuyên Việt Nam", "Trường chuyên Hà Nội - Amsterdam",
            "Trường THPT chuyên Lê Hồng Phong", "Trường THPT chuyên Trần Đại Nghĩa",
            "Giải thưởng khoa học Việt Nam", "Giải thưởng Hồ Chí Minh về khoa học công nghệ",
            "Cuộc thi khoa học kỹ thuật", "Olympic Toán học Việt Nam", "Olympic Tin học Việt Nam",

            # ==================== THỂ THAO (SPORTS) ====================
            "Thể thao Việt Nam", "Việt Nam tại các kỳ Thế vận hội", "Việt Nam tại Đại hội Thể thao Đông Nam Á",
            "Bóng đá tại Việt Nam", "Đội tuyển bóng đá quốc gia Việt Nam", "Giải bóng đá Vô địch Quốc gia Việt Nam",
            "Bóng chuyền tại Việt Nam", "Cầu lông tại Việt Nam", "Võ thuật Việt Nam", "Vovinam",
            "Vật cổ truyền Việt Nam",
            "Cờ tướng", "Điền kinh tại Việt Nam",
            "Thể thao Olympic Việt Nam", "Thể thao SEA Games", "Thể thao ASIAD", "Thể thao Paralympic",
            "Ủy ban Olympic Việt Nam", "Tổng cục Thể dục Thể thao Việt Nam", "Bộ Văn hóa, Thể thao và Du lịch",
            "Vận động viên Việt Nam", "Huấn luyện viên Việt Nam", "Trọng tài thể thao Việt Nam",
            "Đội tuyển bóng đá nữ quốc gia Việt Nam", "Đội tuyển bóng đá U23 Việt Nam",
            "Câu lạc bộ bóng đá Việt Nam", "V.League", "Giải hạng Nhất Quốc gia", "Cúp Quốc gia Việt Nam",
            "CLB Hà Nội", "CLB Thành phố Hồ Chí Minh", "CLB Hoàng Anh Gia Lai", "CLB Sông Lam Nghệ An",
            "Sân vận động Quốc gia Mỹ Đình", "Sân vận động Thống Nhất", "Sân vận động Hàng Đẫy",
            "Bóng chuyền nam Việt Nam", "Bóng chuyền nữ Việt Nam", "Giải vô địch bóng chuyền Việt Nam",
            "Cầu lông Việt Nam", "Giải cầu lông quốc gia", "Vận động viên cầu lông Việt Nam",
            "Tennis Việt Nam", "Quần vợt Việt Nam", "Bóng bàn Việt Nam", "Cờ vua Việt Nam",
            "Cờ tướng Việt Nam", "Cờ úp Việt Nam", "Bơi lội Việt Nam", "Đua thuyền Việt Nam",
            "Thể hình Việt Nam", "Yoga Việt Nam", "Marathon Việt Nam", "Chạy bộ Việt Nam",
            "Đạp xe Việt Nam", "Leo núi Việt Nam", "Bóng rổ Việt Nam", "Bóng ném Việt Nam",
            "Đấu kiếm Việt Nam", "Judo Việt Nam", "Karate Việt Nam", "Taekwondo Việt Nam",
            "Muay Việt Nam", "Vật Việt Nam", "Pencak Silat Việt Nam",

            # ==================== THÀNH PHỐ LỚN (63 TỈNH THÀNH) ====================
            # Thành phố trực thuộc trung ương
            "Thành phố Hồ Chí Minh", "Hà Nội", "Đà Nẵng", "Hải Phòng", "Cần Thơ",

            # Thành phố tỉnh lỵ - Miền Bắc
            "Hạ Long", "Móng Cái", "Uông Bí", "Cẩm Phả", "Hà Giang", "Cao Bằng", "Bắc Kạn",
            "Tuyên Quang", "Lào Cai", "Yên Bái", "Thái Nguyên", "Lạng Sơn", "Bắc Giang",
            "Phú Thọ", "Việt Trì", "Vĩnh Yên", "Bắc Ninh", "Hải Dương", "Hưng Yên", "Thái Bình",
            "Nam Định", "Ninh Bình", "Hà Nam", "Phủ Lý", "Hòa Bình", "Sơn La", "Điện Biên Phủ",
            "Lai Châu", "Lào Cai",

            # Thành phố - Miền Trung
            "Thanh Hóa", "Nghệ An", "Vinh", "Hà Tĩnh", "Đồng Hới", "Huế", "Quảng Trị",
            "Đông Hà", "Tam Kỳ", "Hội An", "Quảng Ngãi", "Quy Nhơn", "Tuy Hòa", "Nha Trang",
            "Phan Rang-Tháp Chàm", "Phan Thiết", "Đà Lạt", "Buôn Ma Thuột", "Pleiku", "Kon Tum",

            # Thành phố - Miền Nam
            "Biên Hòa", "Vũng Tàu", "Long Xuyên", "Châu Đốc", "Rạch Giá", "Hà Tiên", "Cà Mau",
            "Bạc Liêu", "Sóc Trăng", "Trà Vinh", "Vĩnh Long", "Mỹ Tho", "Bến Tre", "Tân An",
            "Cao Lãnh", "Sa Đéc", "Tây Ninh", "Thủ Dầu Một", "Biên Hòa",

            # ==================== DI TÍCH LỊCH SỬ - VĂN HÓA (500+) ====================
            # Hà Nội
            "Lăng Chủ tịch Hồ Chí Minh", "Văn Miếu Quốc Tử Giám", "Hồ Hoàn Kiếm", "Chùa Một Cột",
            "Hoàng thành Thăng Long", "Phố cổ Hà Nội", "Đền Ngọc Sơn", "Nhà thờ Lớn Hà Nội",
            "Chùa Trấn Quốc", "Lăng Chủ tịch Hồ Chí Minh", "Nhà sàn Bác Hồ", "Bảo tàng Hồ Chí Minh",
            "Bảo tàng Lịch sử Quốc gia", "Bảo tàng Mỹ thuật Việt Nam", "Bảo tàng Dân tộc học Việt Nam",
            "Bảo tàng Phụ nữ Việt Nam", "Nhà hát Lớn Hà Nội", "Cầu Long Biên", "Phủ Tây Hồ",
            "Đền Quán Thánh", "Chùa Hà", "Chùa Tây Phương", "Chùa Thầy", "Chùa Hương",
            "Đền Hùng", "Cố đô Hoa Lư", "Tràng An", "Tam Cốc - Bích Động", "Bái Đính",
            "Động Hương Tích", "Chợ Đồng Xuân", "Phố Hàng Mã", "Phố Hàng Đào", "Phố Hàng Gai",
            "Cầu Thê Húc", "Tháp Rùa", "Đền Bạch Mã", "Đình Kim Ngân", "Phố Tạ Hiện",

            # Thành phố Hồ Chí Minh
            "Bảo tàng Chứng tích Chiến tranh", "Dinh Độc Lập", "Nhà thờ Đức Bà", "Chợ Bến Thành",
            "Bưu điện Trung tâm Sài Gòn", "Nhà hát Thành phố", "Phố đi bộ Nguyễn Huệ", "Bến Nhà Rồng",
            "Dinh Thống Nhất", "Bảo tàng Thành phố Hồ Chí Minh", "Bảo tàng Mỹ thuật", "Bảo tàng Áo dài",
            "Chùa Vĩnh Nghiêm", "Chùa Giác Lâm", "Chùa Xá Lợi", "Nhà thờ Tân Định", "Nhà thờ Cha Tam",
            "Địa đạo Củ Chi", "Căn cứ Rừng Sác", "Nhà thờ Huyện Sỹ", "Chợ Bình Tây", "Phố Tàu Sài Gòn",
            "Khu du lịch Suối Tiên", "Công viên Đầm Sen", "Công viên Tao Đàn", "Công viên 23 tháng 9",
            "Phố Bùi Viện", "Chợ An Đông", "Chợ Tân Định", "Dinh Độc Lập", "Thảo Cầm Viên Sài Gòn",

            # Huế
            "Hoàng thành Huế", "Đại Nội Huế", "Ngọ Môn", "Điện Thái Hòa", "Tử Cấm Thành Huế",
            "Lăng Tự Đức", "Lăng Khải Định", "Lăng Minh Mạng", "Lăng Gia Long", "Lăng Thiệu Trị",
            "Chùa Thiên Mụ", "Đền Hòn Chén", "Sông Hương", "Cầu Trường Tiền", "Động Thiên Đường",
            "Bảo tàng Cổ vật Cung đình Huế", "Bảo tàng Mỹ thuật Huế", "Chùa Từ Hiếu", "Chùa Từ Đàm",
            "Đồi Vọng Cảnh", "Hồ Tịnh Tâm", "Phố cổ Huế", "Chợ Đông Ba", "Bến Ngự",

            # Đà Nẵng
            "Cầu Rồng (Đà Nẵng)", "Cầu Vàng (Đà Nẵng)", "Bà Nà Hills", "Ngũ Hành Sơn",
            "Bảo tàng Điêu khắc Chăm", "Bảo tàng Đà Nẵng", "Chùa Linh Ứng", "Đèo Hải Vân",
            "Bãi biển Mỹ Khê", "Bãi biển Non Nước", "Cầu Thuận Phước", "Cầu Trần Thị Lý",
            "Chợ Hàn", "Chợ Cồn", "Bán đảo Sơn Trà", "Làng đá Non Nước", "Phố cổ Hội An",

            # Hội An
            "Phố cổ Hội An", "Chùa Cầu", "Hội quán Phúc Kiến", "Hội quán Quảng Đông",
            "Hội quán Triều Châu", "Nhà cổ Tấn Ký", "Nhà cổ Phùng Hưng", "Nhà cổ Quân Thắng",
            "Bảo tàng Văn hóa Dân gian Hội An", "Bảo tàng Gốm sứ Mậu dịch Hội An", "Chợ Hội An",
            "Bãi biển An Bàng", "Bãi biển Cửa Đại", "Làng rau Trà Quế", "Làng gốm Thanh Hà",
            "Cù Lao Chàm", "Rừng dừa Bảy Mẫu", "Chùa Bà Mụ", "Đảo Hòn Lao",

            # Nha Trang
            "Vịnh Nha Trang", "Hòn Chồng", "Tháp Bà Ponagar", "Nhà thờ Núi Nha Trang",
            "Viện Hải dương học Nha Trang", "Bảo tàng Khánh Hòa", "Vinpearl Land Nha Trang",
            "Hòn Mun", "Hòn Tằm", "Hòn Miễu", "Hòn Một", "Đảo Khỉ", "Đảo Hoa Lan",
            "Bãi biển Nha Trang", "Bãi Dài", "Bãi Dứa", "Chùa Long Sơn", "Tượng Phật Trắng",
            "Vinpearl Safari", "Thác Yangbay", "Suối Hoa Lan", "Hòn Lao",

            # Đà Lạt
            "Hồ Xuân Hương", "Dinh Bảo Đại", "Nhà thờ Con Gà", "Ga Đà Lạt", "Quảng trường Lâm Viên",
            "Chợ Đà Lạt", "Thung lũng Tình yêu", "Đồi Cù", "Đồi Mộng Mơ", "Đồi chè Cầu Đất",
            "Thác Datanla", "Thác Pongour", "Thác Cam Ly", "Hồ Tuyền Lâm", "Thiền viện Trúc Lâm",
            "Chùa Linh Phước", "Chùa Linh Sơn", "Vườn hoa Đà Lạt", "Đồi Mimosa", "Langbiang",
            "Quán Xưa", "Crazy House", "Đồi Robin", "Cầu Đất Farm", "Mê Linh Coffee Garden",

            # Phú Quốc
            "Bãi Sao", "Bãi Dài", "Bãi Ông Lang", "Bãi Vòng", "Bãi Thơm", "Bãi Gành Dầu",
            "Vinpearl Safari Phú Quốc", "VinWonders Phú Quốc", "Dinh Cậu", "Chùa Hộ Quốc",
            "Nhà tù Phú Quốc", "Nhà thùng nước mắm", "Chợ đêm Phú Quốc", "Hòn Thơm", "Hòn Móng Tay",
            "Cáp treo Hòn Thơm", "Sunset Sanato", "Grand World Phú Quốc", "Corona Casino",

            # Vũng Tàu
            "Tượng Chúa Kitô Vua", "Ngọn hải đăng Vũng Tàu", "Bãi Trước", "Bãi Sau", "Bãi Dứa",
            "Bãi Dâu", "Mũi Nghinh Phong", "Núi Lớn", "Núi Nhỏ", "Bạch Dinh", "Biệt thự Cảnh Dương",
            "Lăng Ông Nam Hải", "Thắng cảnh Hồ Mây", "Khu tưởng niệm Bà Rịa - Vũng Tàu", "Bảo tàng Vũng Tàu",

            # Cần Thơ
            "Chợ nổi Cái Răng", "Chợ nổi Phong Điền", "Bến Ninh Kiều", "Chùa Ông", "Chùa Munirensay",
            "Nhà cổ Bình Thủy", "Bảo tàng Cần Thơ", "Chợ Cần Thơ", "Cầu Cần Thơ", "Vườn cò Bằng Lăng",

            # Quảng Ninh
            "Vịnh Hạ Long", "Động Thiên Cung", "Động Đầu Gỗ", "Hang Sửng Sốt", "Hang Luồn",
            "Đảo Titop", "Đảo Cát Bà", "Vườn quốc gia Cát Bà", "Vịnh Lan Hạ", "Vịnh Bái Tử Long",
            "Hồ Ba Bể", "Cô Tô", "Bãi Cháy", "Tuần Châu", "Cầu Bãi Cháy",

            # Ninh Bình
            "Tràng An", "Tam Cốc - Bích Động", "Cố đô Hoa Lư", "Chùa Bái Đính", "Hang Múa",
            "Vườn chim Thung Nham", "Vườn quốc gia Cúc Phương", "Động Thiên Hà", "Đền Trần",

            # Lào Cai
            "Sapa", "Bản Cát Cát", "Đỉnh Fansipan", "Thị trấn Sapa", "Bản Tả Van", "Bản Lao Chải",
            "Thác Bạc Sapa", "Thác Tình Yêu", "Núi Hàm Rồng", "Cổng Trời Sapa", "Nhà thờ Đá Sapa",

            # Hà Giang
            "Cao nguyên đá Đồng Văn", "Dinh Vua Mèo", "Cột cờ Lũng Cú", "Đèo Mã Pì Lèng",
            "Dòng sông Nho Quế", "Thị trấn Đồng Văn", "Thị trấn Mèo Vạc", "Phố cổ Đồng Văn",

            # Quảng Bình
            "Động Phong Nha", "Hang Sơn Đoòng", "Hang Én", "Động Thiên Đường", "Hang Tối",
            "Vườn quốc gia Phong Nha-Kẻ Bàng", "Biển Nhật Lệ", "Thành cổ Quảng Trị",

            # Quảng Nam
            "Khu đền tháp Mỹ Sơn", "Thánh địa Mỹ Sơn", "Bán đảo Sơn Trà", "Cù Lao Chàm",
            "Rừng dừa Bảy Mẫu", "Làng gốm Thanh Hà", "Làng rau Trà Quế",

            # Thừa Thiên Huế
            "Thành nhà Hồ", "Đèo Hải Vân", "Bãi biển Lăng Cô", "Bãi biển Thuận An",
            "Sông Hương", "Đầm Chuồn", "Suối Voi", "Hải Vân Quan",

            # Bình Thuận
            "Mũi Né", "Đồi cát bay", "Đồi cát vàng", "Suối Tiên", "Suối Hồng", "Hòn Rơm",
            "Tháp Chàm Po Sha Inu", "Bảo tàng Văn hóa Chăm", "Hải đăng Kê Gà",

            # Khánh Hòa
            "Vịnh Vân Phong", "Đảo Hòn Tre", "Đảo Hòn Tằm", "Đảo Điệp Sơn", "Đảo Bình Hưng",
            "Bãi Dương", "Đảo Robinson", "Bảo tàng Yersin", "Nhà thờ Núi",

            # Lâm Đồng
            "Thác Prenn", "Thác Pongour", "Thác Voi", "Thác Cam Ly", "Hồ Đại Lải",
            "Hồ Lắk", "Làng Cù Lần", "Làng Lạc Dương", "Hồ Tuyền Lâm",

            # Kon Tum
            "Nhà rông Kon Klor", "Làng Kon K'Tu", "Tu viện Kon Tum", "Cầu treo Kon Klor",
            "Cầu Mây", "Cầu Tre", "Thác Tơ Nưng", "Thác Pa Sỹ",

            # Gia Lai
            "Biển Hồ Pleiku", "Chùa Minh Thành", "Núi Hàm Rồng", "Công viên Đá Bia",
            "Cảng Hàng không Pleiku", "Thác Pơ Cơm", "Khu du lịch Ayun Hạ",

            # Đắk Lắk
            "Thác Dray Nur", "Thác Dray Sap", "Thác Gia Long", "Hồ Lắk", "Làng cổ Đắk Lắk",
            "Nhà rông Đắk Lắk", "Bảo tàng Đắk Lắk", "Biển Hồ",

            # Bà Rịa - Vũng Tàu
            "Hòn Bà", "Hòn Ngư", "Hòn Cau", "Mũi Né", "Bãi Rạng", "Bãi Sau", "Bãi Trước",

            # Đồng Nai
            "Thiền viện Trúc Lâm Viên Nghiêm", "Vườn quốc gia Nam Cát Tiên", "Hồ Trị An",

            # Bình Dương
            "Chùa Hội Khánh", "Khu di tích Bến Đình", "Hồ Dầu Tiếng",

            # Long An
            "Đồng Tháp Mười", "Tràm Chim", "Khu di tích Địa đạo Củ Chi",

            # Tiền Giang
            "Chợ nổi Cái Bè", "Vườn cò Thới Sơn", "Cù lao Thới Sơn", "Chợ Mỹ Tho",

            # Bến Tre
            "Cù lao An Bình", "Làng nghề dừa Bến Tre", "Chùa Vĩnh Tràng", "Phú Lễ",

            # An Giang
            "Núi Sam", "Chùa Tây An", "Chùa Hang", "Miếu Bà Chúa Xứ", "Rừng tràm Trà Sư",
            "Chợ nổi Long Xuyên", "Làng nổi Châu Đốc", "Tịnh xá Ngọc Hồ",

            # Kiên Giang
            "Hòn Đất", "Hòn Đỏ", "Hòn Rồng", "Hòn Sơn", "Hòn Tre", "U Minh Thượng",
            "Mũi Gành Dầu", "Đảo Nam Du", "Hải đăng Rạch Vẹm",

            # Cà Mau
            "Mũi Cà Mau", "U Minh Hạ", "Rừng U Minh", "Đầm Thị Tường", "Chùa Khmer",

            # Bạc Liêu
            "Nhà công tử Bạc Liêu", "Chùa Xiêm Cán", "Vườn chim Bạc Liêu", "Biển Bạc Liêu",

            # Sóc Trăng
            "Chùa Dơi", "Chùa Đất Sét", "Chùa Đất", "Chùa Khmer Sóc Trăng",

            # Trà Vinh
            "Chùa Cổ Trà Vinh", "Chùa Âng", "Chùa Kompong Chrây", "Biển Ba Động",

            # Vĩnh Long
            "Cù lao An Bình", "Chợ nổi Vĩnh Long", "Vườn trái cây Vĩnh Long",

            # Đồng Tháp
            "Vườn quốc gia Tràm Chim", "Rừng Tràm Trà Sư", "Đồng Tháp Mười",

            # Hậu Giang
            "Chợ nổi Ngã Bảy", "Chùa Hậu Giang", "Vườn cò Hậu Giang",

            # ==================== BẢO TÀNG (200+) ====================
            "Bảo tàng Lịch sử Quốc gia", "Bảo tàng Cách mạng Việt Nam", "Bảo tàng Hồ Chí Minh",
            "Bảo tàng Dân tộc học Việt Nam", "Bảo tàng Phụ nữ Việt Nam", "Bảo tàng Mỹ thuật Việt Nam",
            "Bảo tàng Quân đội", "Bảo tàng Không quân", "Bảo tàng Hải quân", "Bảo tàng Công an",
            "Bảo tàng Văn hóa các dân tộc Việt Nam", "Bảo tàng Áo dài Sài Gòn", "Bảo tàng Thành phố Hồ Chí Minh",
            "Bảo tàng Chứng tích Chiến tranh", "Bảo tàng Mỹ thuật Thành phố Hồ Chí Minh",
            "Bảo tàng Lịch sử Thành phố Hồ Chí Minh",
            "Bảo tàng Tôn Đức Thắng", "Bảo tàng Hội An", "Bảo tàng Gốm sứ Mậu dịch Hội An",
            "Bảo tàng Văn hóa Dân gian Hội An", "Bảo tàng Điêu khắc Chăm", "Bảo tàng Đà Nẵng",
            "Bảo tàng Cổ vật Cung đình Huế", "Bảo tàng Mỹ thuật Huế", "Bảo tàng Hà Nội",
            "Bảo tàng Văn học Việt Nam", "Bảo tàng Dân tộc học", "Bảo tàng Thiên nhiên Việt Nam",
            "Bảo tàng Địa chất", "Bảo tàng Nông nghiệp", "Bảo tàng Y học", "Bảo tàng Báo chí",
            "Bảo tàng Bưu chính", "Bảo tàng Đường sắt", "Bảo tàng Hàng hải", "Bảo tàng Hàng không",

            # Bảo tàng các tỉnh
            "Bảo tàng Quảng Ninh", "Bảo tàng Hải Phòng", "Bảo tàng Thái Bình", "Bảo tàng Nam Định",
            "Bảo tàng Ninh Bình", "Bảo tàng Thanh Hóa", "Bảo tàng Nghệ An", "Bảo tàng Hà Tĩnh",
            "Bảo tàng Quảng Bình", "Bảo tàng Quảng Trị", "Bảo tàng Khánh Hòa", "Bảo tàng Bình Định",
            "Bảo tàng Phú Yên", "Bảo tàng Ninh Thuận", "Bảo tàng Bình Thuận", "Bảo tàng Lâm Đồng",
            "Bảo tàng Đắk Lắk", "Bảo tàng Gia Lai", "Bảo tàng Kon Tum", "Bảo tàng Đồng Nai",
            "Bảo tàng Bà Rịa - Vũng Tàu", "Bảo tàng Bình Dương", "Bảo tàng Bình Phước", "Bảo tàng Tây Ninh",
            "Bảo tàng Long An", "Bảo tàng Tiền Giang", "Bảo tàng Bến Tre", "Bảo tàng Vĩnh Long",
            "Bảo tàng Đồng Tháp", "Bảo tàng An Giang", "Bảo tàng Kiên Giang", "Bảo tàng Cần Thơ",
            "Bảo tàng Hậu Giang", "Bảo tàng Sóc Trăng", "Bảo tàng Trà Vinh", "Bảo tàng Bạc Liêu",
            "Bảo tàng Cà Mau", "Bảo tàng Lào Cai", "Bảo tàng Điện Biên", "Bảo tàng Lai Châu",
            "Bảo tàng Sơn La", "Bảo tàng Hòa Bình", "Bảo tàng Yên Bái", "Bảo tàng Tuyên Quang",
            "Bảo tàng Phú Thọ", "Bảo tàng Thái Nguyên", "Bảo tàng Bắc Kạn", "Bảo tàng Cao Bằng",
            "Bảo tàng Lạng Sơn", "Bảo tàng Bắc Giang", "Bảo tàng Bắc Ninh", "Bảo tàng Hưng Yên",
            "Bảo tàng Hải Dương", "Bảo tàng Vĩnh Phúc", "Bảo tàng Hà Nam",

            # Bảo tàng chuyên đề
            "Bảo tàng Hồ Chí Minh tại Nghệ An", "Bảo tàng Hồ Chí Minh tại Thành phố Hồ Chí Minh",
            "Bảo tàng Tội ác chiến tranh", "Bảo tàng Chiến thắng Điện Biên Phủ", "Bảo tàng Chiến thắng Đông Xuân",
            "Bảo tàng Chiến thắng B52", "Bảo tàng Nhà tù Hỏa Lò", "Bảo tàng Nhà tù Côn Đảo",
            "Bảo tàng Nhà tù Phú Quốc", "Bảo tàng Địa đạo Củ Chi", "Bảo tàng Lịch sử Tự nhiên",
            "Bảo tàng Khảo cổ học", "Bảo tàng Nhạc cụ", "Bảo tàng Gốm sứ", "Bảo tàng Lụa",

            # ==================== CHÙA - ĐỀN - MIẾU (1000+) ====================
            # Chùa Hà Nội
            "Chùa Trấn Quốc", "Chùa Một Cột", "Chùa Hà", "Chùa Tây Phương", "Chùa Thầy",
            "Chùa Hương", "Chùa Dâu", "Chùa Quán Sứ", "Chùa Kim Liên", "Chùa Phúc Khánh",
            "Chùa Láng", "Chùa Linh Quang", "Chùa Bà Đanh", "Chùa Vĩnh Nghiêm Hà Nội",
            "Chùa Bà Mu", "Chùa Ông Hoàng", "Chùa Hai Bà Trưng", "Chùa Thái Học",

            # Đền Hà Nội
            "Đền Ngọc Sơn", "Đền Quán Thánh", "Đền Bạch Mã", "Đền Hùng", "Đền Hai Bà Trưng",
            "Đền Bà Triệu", "Đền Trần", "Đền Bà Đen", "Đền Đô", "Đền Sóc",
            "Đền Lạc Long Quân", "Đền Mẫu Thoải", "Đền Mẫu Âu Cơ", "Đền Thượng", "Đền Trung", "Đền Hạ",

            # Chùa Thành phố Hồ Chí Minh
            "Chùa Vĩnh Nghiêm", "Chùa Giác Lâm", "Chùa Xá Lợi", "Chùa Ấn Quang", "Chùa Phước Hải",
            "Chùa Bà Thiên Hậu", "Chùa Ông", "Chùa Bà", "Chùa Pháp Hoa", "Chùa Phổ Quang",
            "Chùa Từ Đàm", "Chùa Phật Học", "Chùa Tây Thiên", "Chùa Hải Đức",

            # Chùa Huế
            "Chùa Thiên Mụ", "Chùa Từ Hiếu", "Chùa Từ Đàm Huế", "Chùa Bảo Quốc", "Chùa Từ Quang",
            "Chùa Thiền Lâm", "Chùa Huyền Không", "Chùa Linh Mụ", "Chùa Chúc Thánh",

            # Chùa Đà Nẵng
            "Chùa Linh Ứng", "Chùa Phước Lâm", "Chùa Quan Âm", "Chùa Phổ Đà", "Chùa Linh Cảm",

            # Chùa các tỉnh miền Bắc
            "Chùa Bút Tháp", "Chùa Dâu", "Chùa Đồi Sơn", "Chùa Phật Tích", "Chùa Keo",
            "Chùa Hàng", "Chùa Bái Đính", "Chùa Tam Chúc", "Chùa Hương Tích", "Chùa Yên Tử",
            "Chùa Hoa Yên", "Chùa Đồng", "Chùa Gióng", "Chùa Hàm Rồng", "Chùa Non Nước",
            "Chùa Pháp Vân", "Chùa Phổ Minh", "Chùa Quảng Đức", "Chùa Tam Thai",

            # Chùa miền Trung
            "Chùa Long Sơn Nha Trang", "Chùa Linh Ẩn Tự", "Chùa Hải Tạng", "Chùa Phước Long",
            "Chùa Ông Núi Sam", "Chùa Hang", "Chùa Tây An", "Chùa Phú Nhuận",

            # Chùa miền Nam
            "Chùa Vĩnh Tràng", "Chùa Tiên", "Chùa Ông Mẹt", "Chùa Phật Học Việt Nam",
            "Chùa Thiên Hậu Sài Gòn", "Chùa Bà Chúa Xứ", "Chùa Khmer", "Chùa Dơi",
            "Chùa Đất Sét", "Chùa Xiêm Cán", "Chùa Kompong Chrây", "Chùa Âng",

            # Nhà thờ Công giáo
            "Nhà thờ Đức Bà Sài Gòn", "Nhà thờ Lớn Hà Nội", "Nhà thờ Đá Phát Diệm",
            "Nhà thờ Tân Định", "Nhà thờ Cha Tam", "Nhà thờ Huyện Sỹ", "Nhà thờ Chợ Quán",
            "Nhà thờ Phùng Khoang", "Nhà thờ Bùi Chu", "Nhà thờ Núi Nha Trang",
            "Nhà thờ Con Gà Đà Lạt", "Nhà thờ Thánh Tâm", "Nhà thờ Hòn Gai", "Nhà thờ Cửa Bắc",
            "Nhà thờ Kiên Lao", "Nhà thờ Bắc Ninh", "Nhà thờ Lạng Sơn", "Nhà thờ Nam Định",

            # Thánh đường Cao Đài
            "Thánh Thất Cao Đài Tây Ninh", "Tòa Thánh Cao Đài", "Thánh Thất Cao Đài Bạc Liêu",
            "Thánh Thất Cao Đài Cần Thơ", "Thánh Thất Cao Đài An Giang",

            # ==================== VƯỜN QUỐC GIA & KHU BẢO TỒN (100+) ====================
            "Vườn quốc gia Cúc Phương", "Vườn quốc gia Ba Vì", "Vườn quốc gia Tam Đảo",
            "Vườn quốc gia Xuân Sơn", "Vườn quốc gia Hoàng Liên", "Vườn quốc gia Ba Bể",
            "Vườn quốc gia Yên Tử", "Vườn quốc gia Bái Tử Long", "Vườn quốc gia Phong Nha-Kẻ Bàng",
            "Vườn quốc gia Bạch Mã", "Vườn quốc gia Bidoup - Núi Bà", "Vườn quốc gia Cát Tiên",
            "Vườn quốc gia Côn Đảo", "Vườn quốc gia Phú Quốc", "Vườn quốc gia U Minh Thượng",
            "Vườn quốc gia U Minh Hạ", "Vườn quốc gia Tràm Chim", "Vườn quốc gia Mũi Cà Mau",
            "Vườn quốc gia Núi Chúa", "Vườn quốc gia Lò Gò - Xa Mát", "Vườn quốc gia Chư Yang Sin",
            "Vườn quốc gia Yok Đôn", "Vườn quốc gia Chu Mom Ray", "Vườn quốc gia Kon Ka Kinh",
            "Vườn quốc gia Vũ Quang", "Vườn quốc gia Xuân Thủy", "Vườn quốc gia Tràm Chim",

            # Khu dự trữ sinh quyển
            "Khu dự trữ sinh quyển Cần Giờ", "Khu dự trữ sinh quyển đồng bằng sông Hồng",
            "Khu dự trữ sinh quyển Tây Nghệ An", "Khu dự trữ sinh quyển Cát Bà",
            "Khu dự trữ sinh quyển Kiên Giang", "Khu dự trữ sinh quyển Cù Lao Chàm",
            "Khu dự trữ sinh quyển Langbiang", "Khu dự trữ sinh quyển núi Chúa",

            # Khu bảo tồn thiên nhiên
            "Khu bảo tồn Sao la", "Khu bảo tồn Pù Mát", "Khu bảo tồn Pù Hoạt",
            "Khu bảo tồn Tà Đùng", "Khu bảo tồn Đakrông", "Khu bảo tồn Sông Thanh",
            "Khu bảo tồn Xuân Liên", "Khu bảo tồn Tây Nghệ An",

            # ==================== BÃI BIỂN (300+) ====================
            # Miền Bắc
            "Bãi Cháy", "Bãi Trà Cổ", "Bãi Quan Lạn", "Bãi Vàn Chảy", "Bãi Cô Tô",
            "Bãi Minh Châu", "Bãi Ngọc Vừng", "Bãi Đồ Sơn", "Bãi Cát Bà", "Bãi Cát Cò",
            "Bãi biển Sầm Sơn", "Bãi biển Hải Tiến", "Bãi biển Thiên Cầm", "Bãi biển Cửa Lò",

            # Miền Trung
            "Bãi biển Lăng Cô", "Bãi biển Thuận An", "Bãi biển Cảnh Dương", "Bãi biển Mỹ Khê",
            "Bãi biển Non Nước", "Bãi biển Phạm Văn Đồng", "Bãi biển An Bàng", "Bãi biển Cửa Đại",
            "Bãi biển Hà My", "Bãi biển Bình Minh", "Bãi biển Mỹ An", "Bãi biển Phước Mỹ",
            "Bãi biển Mỹ Khê Quảng Ngãi", "Bãi biển Sa Huỳnh", "Bãi biển Quy Nhơn",
            "Bãi biển Kỳ Co", "Bãi biển Eo Gió", "Bãi biển Bãi Xép", "Bãi biển Hòn Khô",
            "Bãi biển Đại Lãnh", "Bãi biển Bãi Môn", "Bãi biển Nha Trang", "Bãi Dài Nha Trang",
            "Bãi Dứa", "Bãi Tiên", "Bãi Trào", "Bãi Đông", "Bãi Tân", "Bãi Trúc",
            "Bãi biển Ninh Chữ", "Bãi biển Vĩnh Hy", "Bãi biển Bình Tiên", "Bãi biển Cà Ná",
            "Bãi biển Phan Thiết", "Bãi biển Mũi Né", "Bãi biển Hòn Rơm", "Bãi biển Kê Gà",

            # Miền Nam
            "Bãi Sau Vũng Tàu", "Bãi Trước Vũng Tàu", "Bãi Dứa Vũng Tàu", "Bãi Dâu",
            "Bãi Hồ Cốc", "Bãi Lộc An", "Bãi Hồ Tràm", "Bãi Long Hải", "Bãi Phước Hải",
            "Bãi Sao Phú Quốc", "Bãi Dài Phú Quốc", "Bãi Ông Lang", "Bãi Vòng", "Bãi Thơm",
            "Bãi Gành Dầu", "Bãi Rạch Vẹm", "Bãi Cửa Cạn", "Bãi Khem", "Bãi Dài",
            "Bãi biển Hà Tiên", "Bãi biển Mũi Nai", "Bãi biển Hòn Chông", "Bãi biển Rạch Giá",
            "Bãi biển Bạc Liêu", "Bãi biển Cà Mau", "Bãi biển Gành Hào", "Bãi biển Côn Đảo",
            "Bãi Nhát", "Bãi Ông Đụng", "Bãi Đầm Trầu",

            # ==================== ĐẢO (200+) ====================
            # Quảng Ninh
            "Đảo Cát Bà", "Đảo Tuần Châu", "Đảo Titop", "Đảo Soi Sim", "Đảo Ti Tốp",
            "Đảo Cô Tô", "Đảo Quan Lạn", "Đảo Ngọc Vừng", "Đảo Trần", "Đảo Bàn Than",
            "Đảo Vàn Chảy", "Đảo Minh Châu", "Đảo Thạnh Lân",

            # Hải Phòng
            "Đảo Cát Hải", "Đảo Cát Ông", "Đảo Đồ Sơn", "Đảo Hòn Dáu",

            # Khánh Hòa
            "Đảo Hòn Tre", "Đảo Hòn Tằm", "Đảo Hòn Mun", "Đảo Hòn Một", "Đảo Hòn Miễu",
            "Đảo Hòn Lao", "Đảo Hòn Nội", "Đảo Hòn Ngoại", "Đảo Hòn Rơm", "Đảo Hòn Ông",
            "Đảo Hòn Chồng", "Đảo Bình Ba", "Đảo Bình Hưng", "Đảo Điệp Sơn", "Đảo Yến",
            "Đảo Khỉ", "Đảo Hoa Lan", "Đảo Robinson",

            # Bình Thuận
            "Đảo Phú Quý", "Đảo Hòn Cau",

            # Kiên Giang
            "Đảo Phú Quốc", "Đảo Hòn Thơm", "Đảo Hòn Móng Tay", "Đảo Hòn Mây Rút",
            "Đảo Nam Du", "Hòn Sơn", "Hòn Tre", "Hòn Đất", "Hòn Đỏ", "Hòn Rồng",
            "Đảo Hải Tặc", "Đảo Mây Rút Ngoài", "Đảo Thơm",

            # Quảng Nam
            "Cù Lao Chàm", "Hòn Lao", "Hòn Đài", "Hòn Khô", "Hòn Tài", "Hòn Mồ", "Hòn Ông",

            # Bà Rịa - Vũng Tàu
            "Đảo Côn Đảo", "Hòn Cau", "Hòn Tằm", "Hòn Bà", "Hòn Tre Lớn", "Hòn Tre Nhỏ",

            # Các đảo khác
            "Đảo Lý Sơn", "Đảo Bé", "Đảo Hòn Khoai", "Đảo Hòn Nghệ", "Đảo Hòn Rớ",

            # ==================== THÁC & SUỐI (300+) ====================
            # Miền Bắc
            "Thác Bạc Sapa", "Thác Tình Yêu Sapa", "Thác Bản Giốc", "Thác Pác Bó", "Thác Khuổi Nhi",
            "Thác Mơ", "Thác Dải Yếm", "Thác Mai Châu", "Thác Mộc Châu", "Thác Gò Lào",
            "Thác Thăng Hen", "Thác Đầu Đẳng", "Thác Phú Cường", "Thác Ba Bể", "Thác Đác Rì",
            "Thác Nà Hang", "Thác Sơn Động", "Thác Đá Tảng", "Thác Chiềng Am", "Thác Chiềng Khạt",

            # Miền Trung
            "Thác Yangbay", "Thác Yangkang", "Thác Hòa Phú", "Thác Voi", "Thác Prenn",
            "Thác Datanla", "Thác Pongour", "Thác Cam Ly", "Thác Liên Khương", "Thác Gougah",
            "Thác Bảy Tầng", "Thác Dambri", "Thác Đray Nur", "Thác Đray Sáp", "Thác Gia Long",
            "Thác Krông Kmar", "Thác Krông Nô", "Thác Bờ Y", "Thác Pa Sỹ", "Thác Tơ Nưng",
            "Thác Pơ Cơm", "Thác Kon Hăng", "Thác Kon Tum", "Thác Mơ", "Thác Sa Vết",

            # Suối
            "Suối Tiên Mũi Né", "Suối Hồng", "Suối Voi", "Suối Đá", "Suối Mơ", "Suối Hoa Lan",
            "Suối Tranh", "Suối Đá Bàn", "Suối Hàng Kia", "Suối Thạch Lâm", "Suối Lê",

            # ==================== ĐỘNG & HANG (200+) ====================
            # Quảng Bình
            "Hang Sơn Đoòng", "Hang Én", "Động Phong Nha", "Động Thiên Đường", "Hang Tối",
            "Hang Va", "Hang Tiên", "Hang Chuột", "Hang Thần", "Hang Tiên Sơn", "Hang Tiên Cảnh",

            # Hạ Long
            "Động Thiên Cung", "Động Đầu Gỗ", "Hang Sửng Sốt", "Hang Luồn", "Hang Trinh Nữ",
            "Hang Trai", "Hang Gái", "Hang Cá", "Hang Trong", "Hang Rồng",

            # Ninh Bình
            "Động Thiên Hà", "Động Bích Động", "Động Địch Lộng", "Hang Múa", "Động Huyền Không",

            # Các tỉnh khác
            "Động Hương Tích", "Động Hương Sơn", "Động Pà Thẻn", "Động Pháp Vân", "Động Hoa Sơn",
            "Động Ngườm Ngao", "Động Puông", "Hang Cọc Ngựa", "Hang Bát", "Hang Múa",

            # ==================== NÚI & ĐỈNH (200+) ====================
            "Fansipan", "Núi Bà Đen", "Núi Chứa Chan", "Núi Tà Cu", "Núi Bà Rá", "Núi Sam",
            "Ngũ Hành Sơn", "Núi Sơn Trà", "Núi Thần Tài", "Langbiang", "Núi Cấm",
            "Núi Bà Nà", "Núi Hàm Rồng Sapa", "Núi Hàm Rồng Mũi Né", "Núi Lớn Vũng Tàu",
            "Núi Nhỏ Vũng Tàu", "Núi Minh Đạm", "Núi Tượng", "Núi Côn Đảo", "Núi Chứa Chan",
            "Đỉnh Pu Ta Leng", "Đỉnh Nhìu Cồ San", "Đỉnh Lảo Thẩn", "Đỉnh Tà Chì Nhù",
            "Đỉnh Phu Xai Lai Leng", "Đỉnh Pu Sí Lung", "Đỉnh Pu Sam Cáp",

            # ==================== HỒ (150+) ====================
            "Hồ Hoàn Kiếm", "Hồ Tây", "Hồ Gươm", "Hồ Ba Bể", "Hồ Núi Cốc", "Hồ Thác Bà",
            "Hồ Trị An", "Hồ Dầu Tiếng", "Hồ Phú Ninh", "Hồ Tuyền Lâm", "Hồ Xuân Hương",
            "Hồ Than Thở", "Hồ Mây", "Hồ Đan Kia-Suối Vàng", "Hồ Đại Lải", "Hồ Đồng Mô",
            "Hồ Cốc", "Hồ Lắk", "Hồ Ea Kao", "Hồ T'Nưng", "Hồ Ayun Hạ",
            "Biển Hồ Pleiku", "Hồ Tịnh Tâm Huế", "Hồ Thuỷ Tiên", "Hồ Truồi",

            # ==================== KHU DU LỊCH & KHU VUI CHƠI (500+) ====================
            # Công viên giải trí
            "VinWonders Phú Quốc", "VinWonders Nha Trang", "Vinpearl Land", "Vinpearl Safari",
            "Sun World Bà Nà Hills", "Sun World Hạ Long Park", "Sun World Fansipan Legend",
            "Suối Tiên Sài Gòn", "Đầm Sen", "Công viên nước Hồ Tây", "Aquatopia Water Park",
            "Khu du lịch Tuần Châu", "Khu du lịch Bãi Cháy", "Khu du lịch FLC Sầm Sơn",
            "FLC Quy Nhơn", "FLC Hạ Long", "Cocobay Đà Nẵng", "Premier Village Phú Quốc",

            # Khu nghỉ dưỡng
            "Amanoi Resort", "Six Senses Ninh Vân Bay", "Angsana Lăng Cô", "Banyan Tree Lăng Cô",
            "InterContinental Đà Nẵng", "Vinpearl Resort & Spa", "Melia Vinpearl",
            "JW Marriott Phú Quốc", "Regent Phú Quốc", "Fusion Resort", "Ana Mandara",

            # Khu du lịch sinh thái
            "Khu du lịch sinh thái Tre Việt", "Khu du lịch sinh thái Cần Giờ", "Rừng Sác",
            "Khu du lịch sinh thái Vườn Xoài", "Làng hoa Sa Đéc", "Vườn trái cây Mỹ Khánh",
            "Làng nghề truyền thống", "Làng gốm Bát Tràng", "Làng lụa Vạn Phúc",

            # ==================== LỊCH TRÌNH & TOUR PHỔ BIẾN ====================
            "Tour Hà Nội - Hạ Long", "Tour Hà Nội - Sapa", "Tour Hà Nội - Ninh Bình",
            "Tour miền Tây", "Tour đồng bằng sông Cửu Long", "Tour Sài Gòn - Phú Quốc",
            "Tour Đà Nẵng - Hội An - Huế", "Tour Nha Trang - Đà Lạt", "Tour Tây Nguyên",
            "Tour Côn Đảo", "Tour Cà Mau - Bạc Liêu", "Tour Hà Giang", "Tour Cao Bằng",
            "Tour Mù Cang Chải", "Tour Điện Biên", "Tour miền núi phía Bắc",

            # ==================== TUYẾN ĐƯỜNG DANH THẮNG ====================
            "Đường Hồ Chí Minh", "Quốc lộ 1A", "Đèo Hải Vân", "Đèo Ô Quy Hồ", "Đèo Khau Phạ",
            "Đèo Mã Pì Lèng", "Đèo Ngang", "Đèo Cả", "Đèo Phượng Hoàng", "Đường ven biển",
            "Dọc miền Trung", "Coastal Road",

            "Dọc miền Trung", "Coastal Road", "Đường Trường Sơn Đông", "Con đường Di sản miền Trung",

            # ==================== ẨM THỰC ĐỊA PHƯƠNG (500+) ====================
            # Món ăn đặc sản các vùng miền
            "Phở Hà Nội", "Bún chả Hà Nội", "Bánh cuốn Thanh Trì", "Chả cá Lã Vọng",
            "Cốm Vòng", "Bánh tôm Hồ Tây", "Bún ốc Hà Nội", "Bún đậu mắm tôm",
            "Bún riêu cua", "Bún thang", "Bánh đúc", "Xôi xéo", "Nem chua Thanh Hóa",
            "Cơm lam Sơn La", "Thắng cố Sapa", "Cá tầm Sapa", "Lợn cắp nách",
            "Thịt trâu gác bếp", "Rượu táo mèo", "Mèn mén", "Thắng dền", "Xôi ngũ sắc",

            "Bún bò Huế", "Cơm hến Huế", "Bánh bèo", "Bánh bột lọc", "Bánh ít",
            "Bánh nậm", "Bánh ram", "Chè Huế", "Mè xửng", "Nem lụi", "Bánh khoái",

            "Mì Quảng", "Cao lầu Hội An", "Bánh xèo Hội An", "Bánh bao bánh vạc",
            "Cơm gà Hội An", "Bánh mì Hội An", "Chè bắp", "Bánh đập",

            "Bún chả cá Nha Trang", "Nem nướng Nha Trang", "Bánh căn", "Bánh xèo Nha Trang",
            "Bún sứa", "Chả cá Nha Trang", "Yến sào Nha Trang", "Hải sản tươi sống",

            "Bánh canh chả cá Phan Thiết", "Bánh xèo tôm nhảy", "Bánh căn Phan Thiết",
            "Lẩu thả", "Gỏi cá mai", "Nước mắm Phan Thiết", "Thanh long Bình Thuận",

            "Lẩu gà lá é", "Nem nướng Đà Lạt", "Bánh tráng nướng", "Bánh ướt lòng gà",
            "Bánh mì xíu mại", "Sữa đậu nành", "Dâu tây Đà Lạt", "Atiso Đà Lạt",
            "Rau Đà Lạt", "Hoa Đà Lạt", "Mứt dâu tằm", "Rượu dâu",

            "Bánh canh cua Phú Quốc", "Gỏi cá trích", "Ghẹ hấp", "Nhum nướng",
            "Cá kèo", "Hàu nướng", "Nước mắm Phú Quốc", "Sim rừng", "Mật ong rừng",

            "Hủ tiếu Nam Vang", "Hủ tiếu Mỹ Tho", "Bánh xèo miền Tây", "Lẩu mắm",
            "Cá linh", "Cá lóc nướng trui", "Cá tai tượng", "Cá thát lát",
            "Bánh tét", "Bánh ít lá gai", "Chả giò", "Gỏi cuốn", "Bò 7 món",
            "Cơm tấm Sài Gòn", "Bánh mì Sài Gòn", "Phở Sài Gòn", "Hủ tiếu Sài Gòn",

            # Quán ăn nổi tiếng
            "Phở 10 Lý Quốc Sư", "Bún chả Đắc Kim", "Bún bò Huế O Lệ", "Cao lầu Bà Bé",
            "Cơm gà Bà Buội", "Bánh mì Phượng", "Bánh mì Bà Lan", "Nem nướng Hòa",

            # ==================== LỄ HỘI (300+) ====================
            # Lễ hội văn hóa truyền thống
            "Lễ hội Chùa Hương", "Lễ hội Đền Hùng", "Lễ hội Chùa Bái Đính", "Lễ hội Chùa Tam Chúc",
            "Lễ hội Hoa Ban", "Lễ hội Cà Phê Buôn Ma Thuột", "Lễ hội Đua Bò Bảy Núi",
            "Lễ hội Cướp Phết", "Lễ hội Lồng Tồng", "Lễ hội Hoa Đào", "Lễ hội Hoa Hồng",
            "Lễ hội Đền Trần", "Lễ hội Đền Lao", "Lễ hội Đền Kiếp Bạc", "Lễ hội Đền Sóc",
            "Lễ hội Chùa Keo", "Lễ hội Chùa Hàng", "Lễ hội Chùa Dâu", "Lễ hội Chùa Bút Tháp",
            "Lễ hội Yên Tử", "Lễ hội Chùa Thầy", "Lễ hội Chùa Tây Phương", "Lễ hội Hương Tích",

            # Lễ hội địa phương
            "Lễ hội Gióng", "Lễ hội Lim", "Lễ hội Hoa Lư", "Lễ hội Tràng An", "Lễ hội Bái Đính",
            "Lễ hội Tam Chúc", "Lễ hội Yên Tử", "Lễ hội Côn Sơn - Kiếp Bạc", "Lễ hội Đền Đô",
            "Lễ hội Phố Hiến", "Lễ hội Keo Hạ", "Lễ hội Trần Thương", "Lễ hội Bắc Lệ",
            "Lễ hội Bà Chúa Kho", "Lễ hội Đền Mẫu Đồng Đăng", "Lễ hội Tây Thiên",
            "Lễ hội Sơn Tinh - Thủy Tinh", "Lễ hội Cầu Bông", "Lễ hội Cầu Ngư",

            # Lễ hội mùa
            "Lễ hội Hoa Đào", "Lễ hội Hoa Ban", "Lễ hội Hoa Phượng", "Lễ hội Hoa Sữa",
            "Lễ hội Hoa Tulip", "Lễ hội Festival Hoa Đà Lạt", "Lễ hội Lavender", "Lễ hội Cà Phê",

            # Lễ hội âm nhạc
            "Festival Âm nhạc Quốc tế", "Festival Jazz", "Festival Rock", "Festival EDM",
            "Lễ hội Áo dài", "Lễ hội Văn hóa ẩm thực", "Lễ hội Đường phố", "Lễ hội Pháo hoa"
        ],
        "articles_per_category": 500,  # Bạn có thể điều chỉnh số này
        "priority": "HIGH"
    }
}
