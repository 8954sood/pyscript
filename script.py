import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://github.com/8954sood" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["green", "red"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "박병준")
write("description", "사람")
write("button", "깃허브")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "1+1": "11",
  "1+'1'": "error",
  " ": " ",
  ".": "."
}
information(informations)
