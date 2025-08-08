<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>우리회사</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      line-height: 1.6;
      background-color: #f9f9f9;
      color: #333;
    }

    header {
      background-color: #004080;
      color: white;
      padding: 20px;
      text-align: center;
    }

    nav {
      background: #022d66;
      padding: 10px;
      text-align: center;
    }

    nav a {
      color: white;
      margin: 0 15px;
      text-decoration: none;
      font-weight: bold;
    }

    section {
      padding: 40px 20px;
      max-width: 900px;
      margin: auto;
    }

    .services {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
    }

    .service {
      flex: 0 1 45%;
      background-color: white;
      margin: 10px 0;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }

    footer {
      background-color: #222;
      color: #ccc;
      text-align: center;
      padding: 20px;
    }

    @media (max-width: 600px) {
      .service {
        flex: 0 1 100%;
      }
    }
  </style>
</head>
<body>

  <header>
    <h1>우리회사</h1>
    <p>고객의 미래를 함께 만드는 기업</p>
  </header>

  <nav>
    <a href="#about">회사소개</a>
    <a href="#services">서비스</a>
    <a href="#contact">연락처</a>
  </nav>

  <section id="about">
    <h2>회사 소개</h2>
    <p>
      우리회사는 혁신적인 기술과 신뢰를 바탕으로 고객과 함께 성장하는 IT 전문 기업입니다.
      2020년 설립 이래 다양한 산업 분야에 솔루션을 제공하고 있습니다.
    </p>
  </section>

  <section id="services">
    <h2>서비스</h2>
    <div class="services">
      <div class="service">
        <h3>웹 개발</h3>
        <p>기업 홈페이지, 쇼핑몰, 포털사이트 등 웹 서비스를 맞춤형으로 개발합니다.</p>
      </div>
      <div class="service">
        <h3>모바일 앱</h3>
        <p>iOS/Android 앱 개발부터 출시까지 모든 과정을 책임집니다.</p>
      </div>
    </div>
  </section>

  <section id="contact">
    <h2>연락처</h2>
    <p>📍 서울특별시 강남구 테헤란로 123</p>
    <p>📞 02-123-4567</p>
    <p>📧 contact@wooricorp.com</p>
  </section>

  <footer>
    <p>© 2025 우리회사. 모든 권리 보유.</p>
  </footer>

</body>
</html>
