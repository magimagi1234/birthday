import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(
    page_title="A Surprise for Ricky ❤️",
    page_icon="💗",
    layout="wide"
)

# -----------------------------
# LOAD FILES FROM assets FOLDER
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"


def get_file_data(filename):
    path = ASSETS_DIR / filename

    if not path.is_file():
        return ""

    with path.open("rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


photo1 = get_file_data("photo1.jpeg")
photo2 = get_file_data("photo2.jpeg")
photo3 = get_file_data("photo3.jpeg")
song = get_file_data("song.mp3")


if not photo1 or not photo2 or not photo3:
    st.warning(
        "One or more photos are missing. Put photo1.jpeg, photo2.jpeg and "
        "photo3.jpeg inside the assets folder."
    )


# -----------------------------
# HTML WEBSITE
# -----------------------------
html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* { box-sizing: border-box; }

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
}

body {
    font-family: Georgia, "Times New Roman", serif;
    overflow: hidden;
    background: #351738;
}

.page {
    width: 100%;
    height: 850px;
    display: none;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    text-align: center;
    padding: 25px;
    position: relative;
    overflow: hidden;
}

.page.active {
    display: flex;
}

.page::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 20% 20%, rgba(255,255,255,.16), transparent 18%),
        radial-gradient(circle at 80% 25%, rgba(255,255,255,.12), transparent 20%),
        radial-gradient(circle at 50% 85%, rgba(255,130,190,.18), transparent 25%);
    pointer-events: none;
}

.content {
    position: relative;
    z-index: 5;
    width: 100%;
    max-width: 900px;
}

.pink {
    color: #ffb6d8;
}

.eyebrow {
    font-size: 15px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #ffe9f4;
    margin-bottom: 12px;
}

.title {
    font-size: 44px;
    font-weight: bold;
    line-height: 1.2;
    color: white;
    text-shadow: 0 5px 20px rgba(0,0,0,.25);
}

.subtitle {
    font-size: 20px;
    color: #ffeaf5;
    line-height: 1.6;
    margin: 12px auto;
    max-width: 650px;
}

button {
    border: none;
    background: linear-gradient(135deg, #ff8fbd, #e95498);
    color: white;
    padding: 14px 30px;
    border-radius: 30px;
    font-size: 17px;
    font-family: inherit;
    cursor: pointer;
    margin-top: 22px;
    box-shadow: 0 8px 25px rgba(255,80,150,.3);
}

button:active {
    transform: scale(.95);
}

/* PAGE 1 */
#page1 {
    background: radial-gradient(circle at center, #fff1f8 0%, #df8db6 35%, #51234d 100%);
}

.heart {
    font-size: 110px;
    cursor: pointer;
    animation: heartbeat 1.3s infinite;
    position: relative;
    z-index: 5;
}

@keyframes heartbeat {
    0%,100% { transform: scale(1); }
    50% { transform: scale(1.14); }
}

.tap {
    color: #fff;
    margin-top: 12px;
    font-size: 17px;
}

/* PAGE 2 */
#page2 {
    background: radial-gradient(circle at center, #fff2f8 0%, #d986b1 30%, #54214e 100%);
}

.cake {
    font-size: 125px;
    animation: float 2s ease-in-out infinite;
}

@keyframes float {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-14px); }
}

/* PAGE 3 */
#page3 {
    background: radial-gradient(circle at center, #713166 0%, #3a1b40 65%, #211329 100%);
}

.balloon-area {
    width: 100%;
    max-width: 600px;
    height: 260px;
    position: relative;
    margin: 5px auto;
}

.balloon {
    position: absolute;
    font-size: 70px;
    animation: balloonFloat 3s ease-in-out infinite;
}

.balloon1 { left: 8%; top: 100px; }
.balloon2 { left: 32%; top: 25px; animation-delay: .5s; }
.balloon3 { right: 30%; top: 115px; animation-delay: 1s; }
.balloon4 { right: 7%; top: 45px; animation-delay: 1.5s; }

@keyframes balloonFloat {
    0%,100% { transform: translateY(0) rotate(-3deg); }
    50% { transform: translateY(-22px) rotate(3deg); }
}

.note {
    background: rgba(255,255,255,.12);
    border: 1px solid rgba(255,255,255,.2);
    padding: 12px 18px;
    margin: 8px auto;
    border-radius: 15px;
    color: white;
    max-width: 480px;
}

/* PAGE 4 */
#page4 {
    background: radial-gradient(circle at center, #78356b 0%, #3d1a43 70%, #211329 100%);
}

.photos {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 18px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.card {
    width: 220px;
    background: #fffafc;
    padding: 9px;
    border-radius: 8px;
    box-shadow: 0 12px 30px rgba(0,0,0,.35);
}

.card:nth-child(1) { transform: rotate(-3deg); }
.card:nth-child(2) { transform: rotate(2deg); }
.card:nth-child(3) { transform: rotate(-1deg); }

.card img {
    width: 100%;
    height: 245px;
    object-fit: cover;
    display: block;
    border-radius: 5px;
}

.caption {
    color: #6a3154;
    font-family: Arial, sans-serif;
    font-weight: bold;
    font-size: 14px;
    padding: 9px 4px 5px;
}

.missing {
    height: 245px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #efd5e2;
    color: #7d4562;
    font-family: Arial, sans-serif;
}

/* PAGE 5 */
#page5 {
    background: radial-gradient(circle at center, #81396f 0%, #431c48 68%, #211329 100%);
}

.envelope {
    font-size: 120px;
    cursor: pointer;
    animation: envelopeFloat 1.5s infinite;
}

@keyframes envelopeFloat {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
}

.letter {
    display: none;
    width: 92%;
    max-width: 620px;
    background: #fff8ed;
    color: #5e3b4b;
    padding: 27px;
    border-radius: 18px;
    box-shadow: 0 15px 45px rgba(0,0,0,.4);
    font-family: Arial, sans-serif;
    font-size: 17px;
    line-height: 1.7;
    position: relative;
    z-index: 10;
}

.letter h2 {
    color: #d34e83;
}

/* PAGE 6 */
#page6 {
    background: radial-gradient(circle at center, #ffb8d7 0%, #913b74 40%, #321634 100%);
}

.final-heart {
    font-size: 110px;
    animation: heartbeat 1.4s infinite;
}

.final-title {
    font-size: 43px;
    font-weight: bold;
    color: white;
    text-shadow: 0 5px 25px rgba(0,0,0,.3);
}

.final-text {
    color: white;
    font-size: 20px;
    margin-top: 12px;
}

/* STARS */
.star {
    position: absolute;
    color: white;
    opacity: .7;
    animation: twinkle 2s infinite alternate;
    z-index: 1;
}

@keyframes twinkle {
    from { opacity: .2; transform: scale(.8); }
    to { opacity: 1; transform: scale(1.2); }
}

/* MOBILE */
@media (max-width: 600px) {
    .page { height: 850px; padding: 18px 12px; }
    .title { font-size: 30px; }
    .subtitle { font-size: 17px; }
    .heart { font-size: 90px; }
    .cake { font-size: 95px; }
    .balloon-area { height: 230px; }
    .balloon { font-size: 52px; }
    .card { width: 145px; }
    .card img, .missing { height: 180px; }
    .caption { font-size: 11px; }
    .envelope { font-size: 95px; }
    .letter { font-size: 15px; padding: 20px; }
    .final-title { font-size: 30px; }
}
</style>
</head>

<body>

<!-- PAGE 1 -->
<div class="page active" id="page1">
    <div class="content">
        <div class="eyebrow">a little surprise for you 💗</div>
        <div class="title">A Surprise for Ricky</div>
        <div class="subtitle">I made something special for you...</div>
        <div class="heart" id="start">💝</div>
        <div class="tap">Tap the heart ✨</div>
    </div>
</div>

<!-- PAGE 2 -->
<div class="page" id="page2">
    <div class="content">
        <div class="eyebrow">it's your special day 🎂</div>
        <div class="cake">🎂</div>
        <div class="title">HAPPY BIRTHDAY<br>RICKY ❤️</div>
        <div class="subtitle">
            Wishing you happiness, success and lots of beautiful moments ✨
        </div>
        <button id="next2">Continue 💗</button>
    </div>
</div>

<!-- PAGE 3 -->
<div class="page" id="page3">
    <div class="content">
        <div class="eyebrow">a few little things 🎈</div>
        <div class="title">For You 💕</div>

        <div class="balloon-area">
            <div class="balloon balloon1">🎈</div>
            <div class="balloon balloon2">🎈</div>
            <div class="balloon balloon3">🎈</div>
            <div class="balloon balloon4">🎈</div>
        </div>

        <div class="note">Your smile is one of the sweetest things ❤️</div>
        <div class="note">You deserve lots of happiness ✨</div>
        <div class="note">Keep smiling and keep being amazing 💗</div>

        <button id="next3">See Our Memories 📸</button>
    </div>
</div>

<!-- PAGE 4 -->
<div class="page" id="page4">
    <div class="content">
        <div class="eyebrow">a walk down memory lane ✨</div>
        <div class="title">Beautiful Memories 💕</div>

        <div class="photos">

            <div class="card">
                __PHOTO1__
                <div class="caption">A little piece of happiness ❤️</div>
            </div>

            <div class="card">
                __PHOTO2__
                <div class="caption">My favourite memory 💗</div>
            </div>

            <div class="card">
                __PHOTO3__
                <div class="caption">One more beautiful moment ✨</div>
            </div>

        </div>

        <button id="next4">One More Thing 💌</button>
    </div>
</div>

<!-- PAGE 5 -->
<div class="page" id="page5">
    <div class="content">
        <div class="eyebrow">one last thing...</div>
        <div class="title">I Have Something For You 💌</div>

        <div class="envelope" id="envelope">💌</div>
        <div class="tap" id="envelopeText">Tap the envelope</div>

        <div class="letter" id="letter">
            <h2>Happy Birthday, Ricky ❤️</h2>

            <p>
                I hope this new year of your life brings you
                lots of happiness, beautiful memories and success. ✨
            </p>

            <p>
                Keep smiling, keep dreaming and keep being
                the wonderful person you are. 💗
            </p>

            <p>
                May every little wish of yours find its way to you. 🎂✨
            </p>

            <p>
                Wishing you the happiest birthday! ❤️
            </p>

            <button id="finalButton">Final Surprise 🎉</button>
        </div>
    </div>
</div>

<!-- PAGE 6 -->
<div class="page" id="page6">
    <div class="content">
        <div class="final-heart">❤️</div>
        <div class="final-title">HAPPY BIRTHDAY RICKY! 🎉</div>
        <div class="final-text">
            Hope your day is as special as you are 💗✨
        </div>
        <div style="font-size:60px;margin-top:25px;">
            🎂 🎈 🎁 💕
        </div>
    </div>
</div>

<audio id="music" loop>
    <source src="data:audio/mpeg;base64,__SONG__" type="audio/mpeg">
</audio>

<script>

function showPage(number) {
    document.querySelectorAll(".page").forEach(function(page) {
        page.classList.remove("active");
    });

    document.getElementById("page" + number).classList.add("active");
}

var music = document.getElementById("music");

document.getElementById("start").addEventListener("click", function() {
    music.play().catch(function() {});
    showPage(2);
});

document.getElementById("next2").addEventListener("click", function() {
    showPage(3);
});

document.getElementById("next3").addEventListener("click", function() {
    showPage(4);
});

document.getElementById("next4").addEventListener("click", function() {
    showPage(5);
});

document.getElementById("envelope").addEventListener("click", function() {
    document.getElementById("envelope").style.display = "none";
    document.getElementById("envelopeText").style.display = "none";
    document.getElementById("letter").style.display = "block";
});

document.getElementById("finalButton").addEventListener("click", function() {
    showPage(6);
    createConfetti();
});

function createConfetti() {

    var emojis = [
        "❤️", "💗", "💕", "🎉",
        "✨", "🎈", "🎁", "🌸"
    ];

    for (var i = 0; i < 90; i++) {

        var item = document.createElement("div");

        item.innerHTML =
            emojis[Math.floor(Math.random() * emojis.length)];

        item.style.position = "fixed";
        item.style.left = Math.random() * 100 + "%";
        item.style.top = "-40px";
        item.style.fontSize =
            (15 + Math.random() * 25) + "px";
        item.style.zIndex = "99999";

        document.body.appendChild(item);

        var duration =
            2200 + Math.random() * 2800;

        item.animate(
            [
                {
                    transform:
                        "translateY(0) rotate(0deg)"
                },
                {
                    transform:
                        "translateY(100vh) rotate(720deg)"
                }
            ],
            {
                duration: duration,
                easing: "linear"
            }
        );

        setTimeout(
            function(el) {
                return function() {
                    el.remove();
                };
            }(item),
            duration
        );
    }
}

function createStars() {

    var pages =
        document.querySelectorAll(".page");

    pages.forEach(function(page) {

        for (var i = 0; i < 22; i++) {

            var star =
                document.createElement("div");

            star.className = "star";
            star.innerHTML = "✦";

            star.style.left =
                Math.random() * 100 + "%";

            star.style.top =
                Math.random() * 100 + "%";

            star.style.fontSize =
                (8 + Math.random() * 12) + "px";

            star.style.animationDelay =
                Math.random() * 2 + "s";

            page.appendChild(star);
        }
    });
}

createStars();

</script>

</body>
</html>
"""


# -----------------------------
# PUT PHOTOS INTO HTML
# -----------------------------
def make_image_tag(data, alt):

    if data:
        return (
            '<img src="data:image/jpeg;base64,'
            + data
            + '" alt="'
            + alt
            + '">'
        )

    return '<div class="missing">Photo not found 💔</div>'


html_code = html_code.replace(
    "__PHOTO1__",
    make_image_tag(photo1, "Memory 1")
)

html_code = html_code.replace(
    "__PHOTO2__",
    make_image_tag(photo2, "Memory 2")
)

html_code = html_code.replace(
    "__PHOTO3__",
    make_image_tag(photo3, "Memory 3")
)

html_code = html_code.replace(
    "__SONG__",
    song
)


# -----------------------------
# SHOW WEBSITE
# -----------------------------
components.html(
    html_code,
    height=850,
    scrolling=False
)
