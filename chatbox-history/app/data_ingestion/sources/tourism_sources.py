# app/data_ingestion/sources/tourism_sources.py

DYNAMIC_SOURCES = {
    "vietnam_tourism": {
        "categories": [
            # ==================== DANH MỤC DU LỊCH CHÍNH (1000+) ====================
            # Du lịch tổng quan
            "Du lịch tại Việt Nam", "Du lịch Việt Nam", "Điểm du lịch Việt Nam", "Khu du lịch Việt Nam",
            "Du lịch sinh thái Việt Nam", "Du lịch văn hóa Việt Nam", "Du lịch tâm linh Việt Nam",
            "Du lịch biển đảo Việt Nam", "Du lịch miền núi Việt Nam", "Du lịch đồng bằng Việt Nam",
            "Du lịch cộng đồng Việt Nam", "Du lịch nông thôn Việt Nam", "Du lịch homestay Việt Nam",
            "Du lịch xanh Việt Nam", "Du lịch bền vững Việt Nam", "Du lịch cao cấp Việt Nam",
            "Du lịch bụi Việt Nam", "Du lịch phượt Việt Nam", "Du lịch gia đình Việt Nam",
            "Du lịch trăng mật Việt Nam", "Du lịch team building Việt Nam", "Du lịch nghỉ dưỡng Việt Nam",
            "Du lịch chữa bệnh Việt Nam", "Du lịch golf Việt Nam", "Du lịch thể thao Việt Nam",
            "Du lịch lặn biển Việt Nam", "Du lịch leo núi Việt Nam", "Du lịch trekking Việt Nam",
            "Du lịch xe máy Việt Nam", "Du lịch ô tô Việt Nam", "Du lịch đạp xe Việt Nam",
            "Du lịch thuyền kayak Việt Nam", "Du lịch dù lượn Việt Nam", "Du lịch bay khinh khí cầu",

            # Thành phố & Tỉnh thành (63 tỉnh)
            "Thành phố Việt Nam", "Tỉnh Việt Nam", "Thành phố trực thuộc trung ương Việt Nam",
            "Du lịch Hà Nội", "Du lịch Thành phố Hồ Chí Minh", "Du lịch Đà Nẵng", "Du lịch Hải Phòng",
            "Du lịch Cần Thơ",
            "Du lịch Quảng Ninh", "Du lịch Lào Cai", "Du lịch Hà Giang", "Du lịch Cao Bằng", "Du lịch Bắc Kạn",
            "Du lịch Tuyên Quang", "Du lịch Lạng Sơn", "Du lịch Thái Nguyên", "Du lịch Bắc Giang", "Du lịch Phú Thọ",
            "Du lịch Vĩnh Phúc", "Du lịch Bắc Ninh", "Du lịch Hải Dương", "Du lịch Hưng Yên", "Du lịch Hà Nam",
            "Du lịch Nam Định", "Du lịch Thái Bình", "Du lịch Ninh Bình", "Du lịch Hòa Bình", "Du lịch Sơn La",
            "Du lịch Điện Biên", "Du lịch Lai Châu", "Du lịch Yên Bái",
            "Du lịch Thanh Hóa", "Du lịch Nghệ An", "Du lịch Hà Tĩnh", "Du lịch Quảng Bình", "Du lịch Quảng Trị",
            "Du lịch Thừa Thiên Huế", "Du lịch Quảng Nam", "Du lịch Quảng Ngãi", "Du lịch Bình Định",
            "Du lịch Phú Yên", "Du lịch Khánh Hòa", "Du lịch Ninh Thuận", "Du lịch Bình Thuận", "Du lịch Lâm Đồng",
            "Du lịch Kon Tum", "Du lịch Gia Lai", "Du lịch Đắk Lắk", "Du lịch Đắk Nông",
            "Du lịch Bà Rịa - Vũng Tàu", "Du lịch Đồng Nai", "Du lịch Bình Dương", "Du lịch Bình Phước",
            "Du lịch Tây Ninh",
            "Du lịch Long An", "Du lịch Tiền Giang", "Du lịch Bến Tre", "Du lịch Vĩnh Long", "Du lịch Đồng Tháp",
            "Du lịch An Giang", "Du lịch Kiên Giang", "Du lịch Hậu Giang", "Du lịch Sóc Trăng", "Du lịch Trà Vinh",
            "Du lịch Bạc Liêu", "Du lịch Cà Mau",

            # Danh lam thắng cảnh
            "Danh lam thắng cảnh Việt Nam", "Danh thắng Việt Nam", "Thắng cảnh Việt Nam",
            "Di sản thiên nhiên Việt Nam", "Di sản văn hóa Việt Nam", "Di sản thế giới tại Việt Nam",
            "Công viên địa chất Việt Nam", "Khu di tích quốc gia đặc biệt",

            # Vịnh & Biển
            "Vịnh Việt Nam", "Bãi biển Việt Nam", "Biển Việt Nam", "Đảo Việt Nam", "Quần đảo Việt Nam",
            "Bãi biển đẹp Việt Nam", "Bãi biển hoang sơ", "Bãi biển sạch đẹp", "Bãi biển an toàn",
            "Vịnh đẹp nhất thế giới", "Vịnh Hạ Long", "Vịnh Lan Hạ", "Vịnh Bái Tử Long", "Vịnh Nha Trang",
            "Vịnh Vân Phong", "Vịnh Xuân Đài", "Vịnh Cam Ranh",

            # Núi & Đồi
            "Núi Việt Nam", "Dãy núi Việt Nam", "Đỉnh núi Việt Nam", "Leo núi Việt Nam", "Trekking Việt Nam",
            "Cao nguyên Việt Nam", "Đồi Việt Nam", "Đèo Việt Nam", "Đèo đẹp Việt Nam",

            # Sông & Hồ
            "Sông Việt Nam", "Hồ Việt Nam", "Hồ nước ngọt", "Hồ nhân tạo", "Hồ tự nhiên",
            "Dòng sông Việt Nam", "Sông ngòi Việt Nam", "Suối Việt Nam", "Thác Việt Nam",

            # Động & Hang
            "Hang động Việt Nam", "Động Việt Nam", "Hang Việt Nam", "Động đẹp nhất Việt Nam",
            "Hang động lớn nhất thế giới", "Hang động kỳ thú", "Tour hang động", "Khám phá hang động",

            # Bảo tàng
            "Bảo tàng tại Việt Nam", "Bảo tàng Việt Nam", "Bảo tàng lịch sử", "Bảo tàng dân tộc học",
            "Bảo tàng mỹ thuật", "Bảo tàng văn hóa", "Bảo tàng chiến tranh", "Bảo tàng cách mạng",
            "Bảo tàng chuyên đề", "Bảo tàng địa phương", "Bảo tàng tư nhân", "Bảo tàng miễn phí",

            # Chùa - Đền - Miếu
            "Chùa tại Việt Nam", "Chùa Việt Nam", "Chùa cổ Việt Nam", "Chùa đẹp Việt Nam",
            "Chùa linh thiêng", "Chùa nổi tiếng", "Chùa Phật giáo", "Thiền viện Việt Nam",
            "Đền thờ Việt Nam", "Đền Việt Nam", "Đền cổ", "Đền linh thiêng", "Miếu thờ Việt Nam",
            "Nhà thờ Việt Nam", "Nhà thờ Công giáo", "Nhà thờ cổ", "Nhà thờ đẹp",
            "Thánh đường Việt Nam", "Giáo đường Việt Nam", "Thánh thất Cao Đài",

            # Kiến trúc & Di tích
            "Kiến trúc Việt Nam", "Kiến trúc cổ Việt Nam", "Công trình kiến trúc", "Kiến trúc độc đáo",
            "Di tích lịch sử Việt Nam", "Di tích văn hóa", "Di tích quốc gia", "Di tích cấp tỉnh",
            "Lăng tẩm Việt Nam", "Lăng vua", "Hoàng cung Việt Nam", "Cung điện Việt Nam",
            "Thành cổ Việt Nam", "Thành nhà", "Thành quách", "Tường thành", "Cổng thành",
            "Dinh thự Việt Nam", "Biệt thự cổ", "Nhà cổ Việt Nam", "Nhà rường", "Nhà sàn",
            "Cầu Việt Nam", "Cầu cổ", "Cầu đẹp", "Cầu nổi tiếng", "Cầu hiện đại",

            # Làng nghề & Văn hóa
            "Làng nghề Việt Nam", "Làng nghề truyền thống", "Làng văn hóa", "Làng du lịch",
            "Làng cổ Việt Nam", "Làng xưa", "Làng quê Việt Nam", "Làng nổi", "Làng chài",
            "Làng gốm", "Làng lụa", "Làng hoa", "Làng rau", "Làng trái cây", "Làng nghề mây tre đan",

            # Vườn quốc gia & Bảo tồn
            "Vườn quốc gia Việt Nam", "Khu bảo tồn thiên nhiên", "Khu dự trữ sinh quyển",
            "Rừng quốc gia", "Rừng nguyên sinh", "Rừng nhiệt đới", "Rừng ngập mặn",
            "Khu sinh thái", "Khu bảo vệ động vật", "Khu bảo vệ thực vật",

            # Ẩm thực du lịch
            "Ẩm thực Việt Nam", "Món ăn Việt Nam", "Đặc sản Việt Nam", "Đặc sản địa phương",
            "Ẩm thực miền Bắc", "Ẩm thực miền Trung", "Ẩm thực miền Nam", "Ẩm thực đường phố",
            "Quán ăn ngon Việt Nam", "Nhà hàng Việt Nam", "Quán cà phê Việt Nam", "Chợ đêm Việt Nam",
            "Chợ nổi Việt Nam", "Chợ truyền thống", "Chợ đầu mối", "Chợ hải sản",
            "Tour ẩm thực", "Du lịch ẩm thực", "Trải nghiệm ẩm thực", "Ẩm thực đặc trưng",

            # Lễ hội
            "Lễ hội Việt Nam", "Lễ hội truyền thống", "Lễ hội dân gian", "Lễ hội văn hóa",
            "Lễ hội tôn giáo", "Lễ hội mùa", "Lễ hội âm nhạc", "Festival Việt Nam",
            "Hội chợ Việt Nam", "Triển lãm Việt Nam", "Sự kiện văn hóa", "Sự kiện du lịch",

            # Hoạt động & Trải nghiệm
            "Hoạt động du lịch", "Trải nghiệm du lịch", "Du lịch mạo hiểm", "Thể thao mạo hiểm",
            "Lặn biển", "Lặn ngắm san hô", "Chèo kayak", "Chèo thuyền", "Đi thuyền", "Du thuyền",
            "Câu cá", "Đi bộ đường dài", "Cắm trại", "Picnic", "BBQ", "Team building",
            "Leo núi", "Chinh phục đỉnh núi", "Nhảy dù", "Dù lượn", "Zipline", "Bungee jumping",
            "Đi ATV", "Đi xe địa hình", "Jeep tour", "Moto tour", "Xe đạp leo núi",

            # Khách sạn & Lưu trú
            "Khách sạn Việt Nam", "Resort Việt Nam", "Homestay Việt Nam", "Hostel Việt Nam",
            "Villa Việt Nam", "Căn hộ dịch vụ", "Nhà nghỉ", "Khách sạn 5 sao", "Khách sạn boutique",
            "Khách sạn gần biển", "Khách sạn trung tâm", "Khách sạn giá rẻ", "Khách sạn cao cấp",

            # Dịch vụ du lịch
            "Công ty du lịch Việt Nam", "Tour du lịch Việt Nam", "Hướng dẫn viên du lịch",
            "Dịch vụ du lịch", "Lữ hành Việt Nam", "Đặt tour du lịch", "Tour trọn gói",
            "Tour tự túc", "Tour du lịch trong nước", "Tour du lịch nước ngoài",
            "Vé máy bay", "Đặt vé máy bay", "Vé tàu", "Vé xe", "Thuê xe du lịch",
            "Xe limousine", "Xe khách", "Taxi du lịch", "Xe đưa đón sân bay",

            # Thông tin du lịch
            "Thông tin du lịch Việt Nam", "Kinh nghiệm du lịch", "Cẩm nang du lịch",
            "Lịch trình du lịch", "Hành trình du lịch", "Điểm đến du lịch", "Địa điểm du lịch",
            "Bản đồ du lịch", "Hướng dẫn du lịch", "Review du lịch", "Đánh giá du lịch",
            "Blog du lịch", "Tạp chí du lịch", "Tin tức du lịch", "Sự kiện du lịch",
            "Khuyến mãi du lịch", "Giảm giá tour", "Voucher du lịch", "Deal du lịch",

            # Mùa du lịch
            "Mùa du lịch Việt Nam", "Thời điểm du lịch", "Du lịch mùa xuân", "Du lịch mùa hè",
            "Du lịch mùa thu", "Du lịch mùa đông", "Du lịch Tết", "Du lịch lễ 30/4",
            "Du lịch nghỉ lễ", "Du lịch cuối tuần", "Du lịch ngày thường",

            # Vùng miền
            "Du lịch miền Bắc", "Du lịch miền Trung", "Du lịch miền Nam", "Du lịch Tây Nguyên",
            "Du lịch Đông Bắc", "Du lịch Tây Bắc", "Du lịch Bắc Trung Bộ", "Du lịch Duyên hải Nam Trung Bộ",
            "Du lịch Đông Nam Bộ", "Du lịch Đồng bằng sông Cửu Long", "Du lịch Đồng bằng sông Hồng",
            "Du lịch vùng cao", "Du lịch vùng núi", "Du lịch vùng biển", "Du lịch miền núi phía Bắc",

            # Đặc biệt
            "Điểm đến hấp dẫn", "Địa điểm check-in", "Điểm chụp ảnh đẹp", "Phông nền đẹp",
            "Điểm đến lý tưởng", "Điểm đến được yêu thích", "Điểm đến nổi tiếng", "Điểm đến mới",
            "Điểm đến ít người biết", "Điểm đến bí mật", "Thiên đường du lịch", "Vùng đất diệu kỳ",

            # Xu hướng du lịch
            "Du lịch 2024", "Du lịch 2025", "Xu hướng du lịch", "Du lịch hot", "Du lịch trending",
            "Du lịch viral", "Du lịch Instagram", "Du lịch TikTok", "Du lịch social media",
            "Du lịch bền vững", "Du lịch xanh", "Du lịch có trách nhiệm", "Du lịch thân thiện môi trường",
        ],
        "articles_per_category": 5000,
        "update_frequency": "daily"
    },

    "rss_feeds": {
        "sources": [
            # === BÁO CHÍ QUỐC GIA UY TÍN (VIỆT NAM) - Bổ sung ===
            "https://vnexpress.net/rss/du-lich.rss",
            "https://vnexpress.net/rss/tin-moi-nhat.rss",
            "https://vnexpress.net/rss/the-gioi.rss",
            "https://vnexpress.net/rss/kinh-doanh.rss",
            "https://vnexpress.net/rss/khoa-hoc.rss",
            "https://vnexpress.net/rss/so-hoa.rss",
            "https://vnexpress.net/rss/the-thao.rss",
            "https://tuoitre.vn/rss/du-lich.rss",
            "https://tuoitre.vn/rss/tin-moi-nhat.rss",
            "https://tuoitre.vn/rss/the-gioi.rss",
            "https://tuoitre.vn/rss/kinh-te.rss",
            "https://tuoitre.vn/rss/nhip-song-so.rss",
            "https://thanhnien.vn/rss/du-lich.rss",
            "https://thanhnien.vn/rss/trang-chu.rss",
            "https://thanhnien.vn/rss/the-gioi.rss",
            "https://thanhnien.vn/rss/tai-chinh-kinh-doanh.rss",
            "https://thanhnien.vn/rss/cong-nghe.rss",
            "https://dantri.com.vn/du-lich.rss",
            "https://dantri.com.vn/trang-chu.rss",
            "https://dantri.com.vn/the-gioi.rss",
            "https://dantri.com.vn/kinh-doanh.rss",
            "https://dantri.com.vn/suc-manh-so.rss",
            "https://vietnamnet.vn/rss/du-lich.rss",
            "https://vietnamnet.vn/rss/tin-moi-nhat.rss",
            "https://vietnamnet.vn/rss/the-gioi.rss",
            "https://vietnamnet.vn/rss/kinh-doanh.rss",
            "https://vietnamnet.vn/rss/cong-nghe.rss",
            "https://nld.com.vn/rss/du-lich.rss",
            "https://nld.com.vn/rss/thoi-su-quoc-te.rss",
            "https://nld.com.vn/rss/kinh-te.rss",
            "https://www.24h.com.vn/upload/rss/dulich.rss",
            "https://www.24h.com.vn/upload/rss/tintucquocte.rss",
            "https://www.24h.com.vn/upload/rss/taichinhbatdongsan.rss",
            "https://www.24h.com.vn/upload/rss/congnghethongtin.rss",
            "https://baomoi.com/du-lich.rss",
            "https://baomoi.com/the-gioi.rss",
            "https://baomoi.com/kinh-te.rss",
            "https://baomoi.com/khoa-hoc-cong-nghe.rss",

            # === BÁO CHÍ CHÍNH THỐNG (VIỆT NAM) ===
            "https://nhandan.vn/rss/the-gioi.rss",
            "https://nhandan.vn/rss/kinh-te.rss",
            "https://nhandan.vn/rss/khoa-hoc-cong-nghe.rss",
            "https://www.qdnd.vn/rss/quoc-te.rss",
            "https://www.qdnd.vn/rss/kinh-te.rss",
            "https://vtv.vn/rss/the-gioi.rss",
            "https://vtv.vn/rss/kinh-te.rss",
            "https://vtv.vn/rss/cong-nghe.rss",
            "https://baochinhphu.vn/rss/the-gioi.rss",
            "https://baochinhphu.vn/rss/kinh-te.rss",

            # === BÁO CHUYÊN NGÀNH KINH TẾ (VIỆT NAM) ===
            "https://cafef.vn/rss/trang-chu.rss",
            "https://cafef.vn/rss/thi-truong-quoc-te.rss",
            "https://cafef.vn/rss/vimo.rss",
            "https://vneconomy.vn/rss.htm",
            "https://vneconomy.vn/rss/the-gioi.rss",
            "https://vneconomy.vn/rss/thi-truong.rss",
            "https://vneconomy.vn/rss/doanh-nghiep.rss",
            "https://nhipcaudautu.vn/rss/the-gioi.rss",
            "https://nhipcaudautu.vn/rss/kinh-doanh.rss",
            "https://forbes.vn/feed/",

            # === BÁO CHUYÊN NGÀNH CÔNG NGHỆ (VIỆT NAM) ===
            "https://vnreview.vn/feed",
            "https://tinhte.vn/rss",
            "https://genk.vn/rss/trang-chu.rss",
            "https://genk.vn/rss/kham-pha.rss",
            "https://soha.vn/du-lich.rss",
            "https://soha.vn/rss/quan-su.rss",
            "https://soha.vn/rss/cong-nghe.rss",

            # === BÁO CHUYÊN NGÀNH VĂN HÓA & GIẢI TRÍ (VIỆT NAM) ===
            "https://travellive.vn/rss",
            "https://afamily.vn/rss/du-lich.rss",
            "https://kenh14.vn/rss/du-lich.rss",
            "https://kenh14.vn/rss/the-gioi.rss",
            "https://kenh14.vn/rss/star.rss",
            "https://baotintuc.vn/rss/van-hoa.rss",
            "https://baotintuc.vn/rss/the-thao.rss",
            "https://elle.vn/feed",

            # === BÁO ĐỊA PHƯƠNG (VIỆT NAM) - Bổ sung ===
            "https://hanoimoi.com.vn/rss/du-lich.rss",
            "https://hanoimoi.com.vn/rss/the-gioi.rss",
            "https://www.sggp.org.vn/rss/du-lich.rss",
            "https://www.sggp.org.vn/rss/the-gioi.rss",
            "https://www.sggp.org.vn/rss/kinh-te.rss",
            "https://baodanang.vn/rss/du-lich.rss",
            "https://baodanang.vn/rss/the-gioi.rss",
            "https://baoquangninh.vn/rss",
            "https://baokhanhhoa.vn/rss/du-lich.rss",
            "https://baokhanhhoa.vn/rss/the-gioi.rss",
            "https://baolongan.vn/rss",
            "https://baocantho.com.vn/rss/the-gioi.rss",

            # ================================================
            # === HÃNG THÔNG TẤN & TIN TỨC QUỐC TẾ (GLOBAL) ===
            # ================================================

            # --- Hãng thông tấn lớn (Wires) ---
            "https://www.reuters.com/arc/outboundfeeds/rss/category/world/",
            "https://www.reuters.com/arc/outboundfeeds/rss/category/business/",
            "https://www.reuters.com/arc/outboundfeeds/rss/category/technology/",
            "https://www.reuters.com/arc/outboundfeeds/rss/category/sports/",
            "https://rss.app/feeds/AP-News.xml",
            "https://feeds.bbci.co.uk/news/world/rss.xml",
            "https://feeds.bbci.co.uk/news/business/rss.xml",
            "https://feeds.bbci.co.uk/news/technology/rss.xml",
            "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
            "https://www.aljazeera.com/xml/rss/all.xml",

            # --- Báo chí uy tín (Mỹ) ---
            "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
            "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
            "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
            "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
            "https://www.wsj.com/xml/rss/3_7085.xml",
            "https://www.wsj.com/xml/rss/3_7014.xml",
            "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml",
            "https://www.washingtonpost.com/wp-srv/xml/rss/world.xml",
            "https://www.washingtonpost.com/wp-srv/xml/rss/business.xml",

            # --- Báo chí uy tín (Anh) ---
            "https://www.theguardian.com/world/rss",
            "https://www.theguardian.com/business/rss",
            "https://www.theguardian.com/technology/rss",
            "https://www.ft.com/rss/world",
            "https://www.ft.com/rss/companies",
            "https://www.economist.com/rss/the-world-this-week",
            "https://www.economist.com/rss/business-and-finance",

            # --- Kinh tế & Tài chính (Quốc tế) ---
            "https://www.bloomberg.com/company/feed/blog/",
            "https://feeds.bloomberg.com/markets/news.rss",
            "https://www.cnbc.com/id/100003114/device/rss/rss.html",
            "https://www.cnbc.com/id/100727362/device/rss/rss.html",
            "https://www.forbes.com/rss/business",
            "https://www.forbes.com/rss/technology",
            "https://hbr.org/rss/regular",

            # --- Công nghệ (Quốc tế) ---
            "https://techcrunch.com/feed/",
            "https://www.theverge.com/rss/index.xml",
            "https://www.wired.com/feed/rss",
            "https://arstechnica.com/feed/",
            "https://news.ycombinator.com/rss",
            "https://www.technologyreview.com/feed/",

            # --- Khoa học & Du lịch (Quốc tế) ---
            "https://www.sciencedaily.com/rss/all.xml",
            "https://www.scientificamerican.com/feed/",
            "https://www.popsci.com/feed/",
            "https://www.nationalgeographic.com/rss-feeds/all-stories",
            "https://www.nationalgeographic.com/rss-feeds/travel",
            "https://www.cntraveler.com/rss"
        ],
        "update_frequency": "daily",
        "retention_days": 90
    }
}
