<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>우리커뮤니티</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
    header { background: #333; color: #fff; padding: 20px; text-align: center; }
    .container { padding: 20px; max-width: 800px; margin: auto; }
    a.board { display: block; background: white; padding: 15px; margin: 10px 0; border-radius: 6px; text-decoration: none; color: #333; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    a.board:hover { background: #eaeaea; }
  </style>
</head>
<body>
  <header>
    <h1>우리커뮤니티 포털</h1>
    <p>다양한 주제의 커뮤니티에 참여하세요</p>
  </header>

  <div class="container">
    <h2>게시판 목록</h2>
    <a href="board.html?category=free" class="board">📢 자유게시판</a>
    <a href="board.html?category=tech" class="board">💻 IT·기술 게시판</a>
    <a href="board.html?category=games" class="board">🎮 게임 게시판</a>
  </div>
</body>
</html>
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>게시판</title>
  <style>
    body { font-family: Arial; background: #fafafa; }
    .container { max-width: 800px; margin: auto; padding: 20px; }
    .post { background: white; margin: 10px 0; padding: 15px; border-radius: 6px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    .post a { text-decoration: none; color: #333; font-weight: bold; }
    .write-btn { margin-top: 20px; display: inline-block; padding: 10px 20px; background: #333; color: white; border-radius: 6px; text-decoration: none; }
  </style>
</head>
<body>
  <div class="container">
    <h1 id="boardTitle">게시판</h1>
    <div id="postList"></div>
    <a href="#" class="write-btn" onclick="alert('글쓰기 기능은 아직 구현되지 않았어요 😅')">+ 새 글 쓰기</a>
  </div>

  <script>
    const params = new URLSearchParams(window.location.search);
    const category = params.get('category') || 'free';

    const boardNames = {
      free: "자유게시판",
      tech: "IT·기술 게시판",
      games: "게임 게시판"
    };

    document.getElementById('boardTitle').innerText = boardNames[category];

    // 예시 게시글 목록
    const dummyPosts = [
      { id: 1, title: "첫 번째 글입니다", author: "익명1" },
      { id: 2, title: "두 번째 글이에요", author: "익명2" }
    ];

    const postList = document.getElementById('postList');
    dummyPosts.forEach(post => {
      const div = document.createElement('div');
      div.className = 'post';
      div.innerHTML = `<a href="post.html?id=${post.id}">${post.title}</a><br><small>작성자: ${post.author}</small>`;
      postList.appendChild(div);
    });
  </script>
</body>
</html>

