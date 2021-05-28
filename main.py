from flask import Flask, request, Response
app = Flask(__name__)

@app.route("/set", methods=["POST"])
def set_px():
    global px_colors
    if request.method == "POST":
        px_x = int(request.form["px_x"])
        px_y = int(request.form["px_y"])
        px_color = request.form["color"]
        px_colors[px_y][px_x] = px_color
    

@app.route("/get", methods=["GET"])
def get_pxs():
    global px_colors
    return Response(str(px_colors))


if __name__ == "__main__":
    global px_colors
    # 设置像素列数和行数
    px_length = 5
    px_height = 5
    px_colors = [[(0, 0, 0) for _ in range(px_length)] for _ in range(px_height)]
    # for px_x in px_colors:
    #     print(px_x)
    app.run("0.0.0.0", 8080)
