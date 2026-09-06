import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(
    page_title="A Surprise for Ricky",
    page_icon="♥",
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

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<style>

/* =========================================
   FONTS
========================================= */

@import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Playfair+Display:wght@600;700&display=swap');


/* =========================================
   BASIC
========================================= */

* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
}

body {

    overflow: hidden;

    background:
        radial-gradient(
            circle at 50% 45%,
            #7d315f 0%,
            #38183b 70%,
            #170d22 100%
        );

    color: white;

    font-family:
        "Patrick Hand",
        "Comic Sans MS",
        cursive;
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


.content {

    position: relative;

    z-index: 20;

    width: 100%;

    max-width: 900px;
}


.title {

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 48px;

    line-height: 1.1;

    color: white;

    text-shadow:
        0 3px 15px rgba(0,0,0,.35);
}


.subtitle {

    font-size: 21px;

    color: #f7dce9;

    margin-top: 12px;

    line-height: 1.5;
}


.eyebrow {

    font-size: 16px;

    color: #f8dce9;

    letter-spacing: 2px;

    margin-bottom: 12px;
}


button {

    border: none;

    outline: none;

    background:
        linear-gradient(
            135deg,
            #ff8dbd,
            #d94e91
        );

    color: white;

    padding: 12px 30px;

    border-radius: 30px;

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 20px;

    cursor: pointer;

    margin-top: 22px;

    box-shadow:
        0 8px 30px rgba(255,80,150,.3);

    transition:
        transform .2s,
        box-shadow .2s;
}


button:hover {

    transform: scale(1.05);

    box-shadow:
        0 12px 35px rgba(255,100,170,.45);
}


/* =========================================
   PAGE 1
   HEART + ARROW + BLAST
========================================= */

#page1 {

    background:
        radial-gradient(
            circle at center,
            #fff7fa 0%,
            #f4b6cf 23%,
            #8c376e 53%,
            #27132e 100%
        );
}


.intro-title {

    font-family:
        "Playfair Display",
        serif;

    font-size: 42px;

    margin-bottom: 8px;
}


.intro-small {

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 21px;

    color: #fff0f7;
}


/* CSS HEART */

.heart-box {

    width: 150px;

    height: 150px;

    position: relative;

    margin: 35px auto 5px;

    cursor: pointer;

    z-index: 30;
}


.css-heart {

    width: 82px;

    height: 82px;

    position: absolute;

    left: 34px;

    top: 32px;

    background: #ff6fae;

    transform:
        rotate(-45deg);

    border-radius:
        12px 0 12px 0;

    box-shadow:
        0 0 35px rgba(255,80,160,.7);

    animation:
        heartbeat 1.2s infinite;
}


.css-heart::before,
.css-heart::after {

    content: "";

    position: absolute;

    width: 82px;

    height: 82px;

    border-radius: 50%;

    background: #ff6fae;
}


.css-heart::before {

    top: -41px;

    left: 0;
}


.css-heart::after {

    left: 41px;

    top: 0;
}


@keyframes heartbeat {

    0%,100% {
        transform: rotate(-45deg) scale(1);
    }

    50% {
        transform: rotate(-45deg) scale(1.12);
    }
}


/* ARROW */

.arrow {

    position: absolute;

    width: 75px;

    height: 3px;

    background: white;

    left: -55px;

    top: 72px;

    transform:
        rotate(-20deg);

    transform-origin: right center;

    opacity: .95;
}


.arrow::after {

    content: "";

    position: absolute;

    right: -1px;

    top: -6px;

    width: 14px;

    height: 14px;

    border-top: 3px solid white;

    border-right: 3px solid white;

    transform:
        rotate(45deg);
}


/* HEART BURST */

.burst {

    position: fixed;

    left: 50%;

    top: 50%;

    width: 20px;

    height: 20px;

    pointer-events: none;

    z-index: 9999;

    display: none;
}


.burst-piece {

    position: absolute;

    left: 0;

    top: 0;

    width: 10px;

    height: 10px;

    background: #ff7db5;

    border-radius: 50%;

    animation:
        burstMove 1.3s ease-out forwards;
}


@keyframes burstMove {

    from {

        transform:
            translate(0,0)
            scale(1);

        opacity: 1;
    }

    to {

        transform:
            translate(
                var(--x),
                var(--y)
            )
            scale(0);

        opacity: 0;
    }
}


.pink-flash {

    position: fixed;

    inset: 0;

    background:
        radial-gradient(
            circle,
            rgba(255,150,200,.95),
            rgba(255,105,170,.75),
            rgba(145,42,104,.8)
        );

    z-index: 9998;

    pointer-events: none;

    opacity: 0;

    transform: scale(.1);
}


.pink-flash.active {

    animation:
        flashSpread 1.3s ease-out forwards;
}


@keyframes flashSpread {

    0% {
        opacity: 1;
        transform: scale(.1);
    }

    60% {
        opacity: .85;
        transform: scale(1.8);
    }

    100% {
        opacity: 0;
        transform: scale(3);
    }
}


/* =========================================
   PAGE 2
   HEART LEAF TREE
========================================= */

#page2 {

    background:
        radial-gradient(
            circle at center,
            #9b416f 0%,
            #521f50 45%,
            #21132d 100%
        );
}


.tree-area {

    width: 360px;

    height: 390px;

    position: relative;

    margin: 5px auto;
}


/* TRUNK */

.trunk {

    position: absolute;

    bottom: 15px;

    left: 50%;

    width: 18px;

    height: 250px;

    background:
        linear-gradient(
            90deg,
            #4b2430,
            #783c45,
            #44202d
        );

    border-radius: 20px;

    transform:
        translateX(-50%)
        rotate(1deg);

    transform-origin: bottom;
}


.branch {

    position: absolute;

    height: 10px;

    background: #5a2936;

    border-radius: 20px;

    transform-origin: left center;
}


.branch.one {

    width: 120px;

    left: 50%;

    top: 100px;

    transform:
        rotate(-35deg);
}


.branch.two {

    width: 110px;

    left: 48%;

    top: 155px;

    transform:
        rotate(32deg);
}


.branch.three {

    width: 85px;

    left: 50%;

    top: 60px;

    transform:
        rotate(30deg);
}


/* HEART LEAVES */

.leaf {

    position: absolute;

    width: 28px;

    height: 28px;

    background: #ef75ae;

    transform:
        rotate(-45deg)
        scale(0);

    border-radius:
        6px 0 6px 0;

    box-shadow:
        0 0 15px rgba(255,100,180,.45);

    animation:
        leafAppear .6s forwards;
}


.leaf::before,
.leaf::after {

    content: "";

    position: absolute;

    width: 28px;

    height: 28px;

    background: #ef75ae;

    border-radius: 50%;
}


.leaf::before {

    top: -14px;
    left: 0;
}


.leaf::after {

    top: 0;
    left: 14px;
}


@keyframes leafAppear {

    to {

        transform:
            rotate(-45deg)
            scale(1);
    }
}


/* leaf positions */

.l1 { left: 105px; top: 70px; animation-delay: .2s; }
.l2 { left: 155px; top: 45px; animation-delay: .35s; }
.l3 { left: 205px; top: 75px; animation-delay: .5s; }
.l4 { left: 80px; top: 125px; animation-delay: .65s; }
.l5 { left: 140px; top: 105px; animation-delay: .8s; }
.l6 { left: 215px; top: 125px; animation-delay: .95s; }
.l7 { left: 110px; top: 160px; animation-delay: 1.1s; }
.l8 { left: 180px; top: 155px; animation-delay: 1.25s; }
.l9 { left: 245px; top: 170px; animation-delay: 1.4s; }


/* =========================================
   PAGE 3
   CAKE
========================================= */

#page3 {

    background:
        radial-gradient(
            circle at center,
            #8e3d70 0%,
            #4c1e4b 55%,
            #21132d 100%
        );
}


.cake-area {

    width: 320px;

    height: 350px;

    position: relative;

    margin: 10px auto;
}


/* CANDLE */

.candle {

    position: absolute;

    width: 15px;

    height: 62px;

    background:
        repeating-linear-gradient(
            135deg,
            #fff,
            #fff 7px,
            #f38bb7 7px,
            #f38bb7 13px
        );

    left: 50%;

    top: 20px;

    transform:
        translateX(-50%)
        translateY(-80px);

    opacity: 0;

    border-radius: 4px;

    transition:
        all .8s ease;
}


.flame {

    position: absolute;

    width: 16px;

    height: 23px;

    background: #ffd16a;

    border-radius:
        50% 50% 50% 0;

    transform:
        rotate(-45deg);

    left: -1px;

    top: -18px;

    box-shadow:
        0 0 18px #ffb347;
}


.cake-area.show .candle {

    transform:
        translateX(-50%)
        translateY(0);

    opacity: 1;
}


/* CAKE PLATES */

.layer {

    position: absolute;

    left: 50%;

    transform:
        translateX(-50%)
        translateY(150px);

    opacity: 0;

    border-radius: 10px;

    box-shadow:
        0 7px 15px rgba(0,0,0,.25);

    transition:
        all .8s ease;
}


.layer1 {

    bottom: 45px;

    width: 260px;

    height: 65px;

    background:
        linear-gradient(
            #e66b9e,
            #b94778
        );
}


.layer2 {

    bottom: 105px;

    width: 220px;

    height: 58px;

    background:
        linear-gradient(
            #f18ab5,
            #d45a91
        );
}


.layer3 {

    bottom: 160px;

    width: 175px;

    height: 52px;

    background:
        linear-gradient(
            #ff9bc2,
            #e36b9f
        );
}


/* CREAM */

.cream {

    position: absolute;

    left: 50%;

    width: 180px;

    height: 16px;

    background: #fff5fa;

    border-radius: 50%;

    transform:
        translateX(-50%)
        translateY(100px);

    opacity: 0;

    transition:
        all .6s ease;
}


.cream1 {
    bottom: 150px;
}


.cream2 {
    bottom: 102px;
}


.cake-area.show .layer1 {

    transform:
        translateX(-50%)
        translateY(0);

    opacity: 1;

    transition-delay: .2s;
}


.cake-area.show .layer2 {

    transform:
        translateX(-50%)
        translateY(0);

    opacity: 1;

    transition-delay: .8s;
}


.cake-area.show .layer3 {

    transform:
        translateX(-50%)
        translateY(0);

    opacity: 1;

    transition-delay: 1.4s;
}


.cake-area.show .cream {

    transform:
        translateX(-50%)
        translateY(0);

    opacity: 1;
}


.cake-area.show .cream1 {

    transition-delay: 1.2s;
}


.cake-area.show .cream2 {

    transition-delay: 1.8s;
}


.cake-area.show .candle {

    transition-delay: 2.3s;
}


.birthday-reveal {

    opacity: 0;

    transform:
        translateY(15px);

    animation:
        birthdayReveal 1s forwards;

    animation-delay: 3s;
}


@keyframes birthdayReveal {

    to {

        opacity: 1;

        transform:
            translateY(0);
    }
}


/* =========================================
   PAGE 4
   BALLOONS
========================================= */

#page4 {

    background:
        radial-gradient(
            circle at center,
            #6e2865 0%,
            #321738 72%,
            #170c20 100%
        );
}


.balloon-area {

    width: 520px;

    max-width: 95%;

    height: 310px;

    position: relative;

    margin: 10px auto;
}


.balloon {

    position: absolute;

    width: 62px;

    height: 78px;

    border-radius:
        50% 50% 48% 48%;

    cursor: pointer;

    transition:
        transform .2s;

    box-shadow:
        inset -8px -8px 15px rgba(0,0,0,.15),
        0 0 18px rgba(255,150,210,.18);

    animation:
        balloonFloat 3s ease-in-out infinite;
}


.balloon:hover {

    transform:
        scale(1.08);
}


.balloon::before {

    content: "";

    position: absolute;

    bottom: -7px;

    left: 27px;

    width: 8px;

    height: 8px;

    background: inherit;

    transform:
        rotate(45deg);
}


.balloon::after {

    content: "";

    position: absolute;

    top: 75px;

    left: 31px;

    width: 1px;

    height: 115px;

    background: rgba(255,255,255,.55);
}


.b1 {

    left: 5%;

    top: 130px;

    background: #f68bb8;

}


.b2 {

    left: 30%;

    top: 45px;

    background: #9e7ce5;

    animation-delay: .4s;
}


.b3 {

    right: 30%;

    top: 115px;

    background: #56c5b6;

    animation-delay: .8s;
}


.b4 {

    right: 5%;

    top: 55px;

    background: #ef895e;

    animation-delay: 1.2s;
}


@keyframes balloonFloat {

    0%,100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-15px);
    }
}


.balloon.popped {

    animation:
        balloonPop .45s forwards;
}


@keyframes balloonPop {

    0% {
        transform: scale(1);
        opacity: 1;
    }

    50% {
        transform: scale(1.35);
        opacity: .7;
    }

    100% {
        transform: scale(0);
        opacity: 0;
    }
}


.balloon-message {

    position: absolute;

    left: 50%;

    top: 42%;

    transform:
        translate(-50%,-50%)
        scale(.7);

    width: 85%;

    max-width: 520px;

    padding: 18px 25px;

    background:
        rgba(255,255,255,.08);

    border:
        1px solid rgba(255,255,255,.22);

    border-radius: 18px;

    font-size: 23px;

    color: #fff0f7;

    opacity: 0;

    pointer-events: none;

    transition:
        all .5s ease;
}


.balloon-message.show {

    opacity: 1;

    transform:
        translate(-50%,-50%)
        scale(1);
}


/* =========================================
   PAGE 5
   PHOTOS
========================================= */

#page5 {

    background:
        radial-gradient(
            circle at center,
            #722d69 0%,
            #351738 70%,
            #180d22 100%
        );
}


.photos {

    display: flex;

    justify-content: center;

    align-items: center;

    gap: 18px;

    flex-wrap: wrap;

    margin-top: 18px;
}


.card {

    width: 220px;

    background: #fffafc;

    padding: 9px;

    border-radius: 7px;

    box-shadow:
        0 12px 30px rgba(0,0,0,.35);
}


.card:nth-child(1) {

    transform: rotate(-3deg);
}


.card:nth-child(2) {

    transform: rotate(2deg);
}


.card:nth-child(3) {

    transform: rotate(-1deg);
}


.card img {

    width: 100%;

    height: 245px;

    object-fit: cover;

    display: block;

    border-radius: 5px;
}


.caption {

    color: #6a3154;

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 17px;

    padding: 8px 4px 5px;
}


.missing {

    height: 245px;

    display: flex;

    justify-content: center;

    align-items: center;

    background: #efd5e2;

    color: #7d4562;

    font-family:
        "Patrick Hand",
        cursive;
}


/* =========================================
   PAGE 6
   ENVELOPE
========================================= */

#page6 {

    background:
        radial-gradient(
            circle at center,
            #713064 0%,
            #361638 70%,
            #180d21 100%
        );
}


.envelope-stage {

    width: 100%;

    height: 250px;

    position: relative;

    overflow: hidden;

    margin-top: 10px;
}


/* CSS ENVELOPE */

.envelope {

    position: absolute;

    left: -180px;

    top: 50%;

    width: 190px;

    height: 125px;

    background: #fff1dc;

    border-radius: 8px;

    box-shadow:
        0 15px 40px rgba(0,0,0,.35);

    transform:
        translateY(-50%);

    transition:
        left 1.4s cubic-bezier(.2,.8,.2,1);

    cursor: pointer;
}


.envelope.center {

    left: 50%;

    transform:
        translate(-50%,-50%);
}


.envelope::before {

    content: "";

    position: absolute;

    left: 0;

    top: 0;

    width: 0;

    height: 0;

    border-left:
        95px solid transparent;

    border-right:
        95px solid transparent;

    border-top:
        65px solid #e8c9a9;
}


.envelope::after {

    content: "";

    position: absolute;

    bottom: 0;

    left: 0;

    width: 0;

    height: 0;

    border-left:
        95px solid transparent;

    border-right:
        95px solid transparent;

    border-bottom:
        70px solid #f8ddc2;
}


.envelope-label {

    position: absolute;

    z-index: 5;

    left: 50%;

    top: 55%;

    transform:
        translate(-50%,-50%);

    color: #9d5271;

    font-size: 19px;
}


.letter {

    display: none;

    width: 92%;

    max-width: 620px;

    background: #fff8ed;

    color: #5e3b4b;

    padding: 27px;

    border-radius: 12px;

    box-shadow:
        0 15px 45px rgba(0,0,0,.4);

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 20px;

    line-height: 1.55;

    position: relative;

    z-index: 100;
}


.letter.show {

    display: block;

    animation:
        letterOpen .7s ease;
}


@keyframes letterOpen {

    from {

        opacity: 0;

        transform:
            scale(.8)
            translateY(20px);
    }

    to {

        opacity: 1;

        transform:
            scale(1)
            translateY(0);
    }
}


.letter h2 {

    color: #c64c80;

    font-size: 30px;
}


/* =========================================
   FINAL PAGE
========================================= */

#page7 {

    background:
        radial-gradient(
            circle at center,
            #b04a80 0%,
            #571f53 50%,
            #20102b 100%
        );
}


.final-heart {

    width: 90px;

    height: 90px;

    background: #ff78ad;

    transform:
        rotate(-45deg);

    margin: 30px auto;

    position: relative;

    animation:
        finalBeat 1.3s infinite;
}


.final-heart::before,
.final-heart::after {

    content: "";

    position: absolute;

    width: 90px;

    height: 90px;

    background: #ff78ad;

    border-radius: 50%;
}


.final-heart::before {

    top: -45px;

    left: 0;
}


.final-heart::after {

    left: 45px;

    top: 0;
}


@keyframes finalBeat {

    0%,100% {
        transform: rotate(-45deg) scale(1);
    }

    50% {
        transform: rotate(-45deg) scale(1.12);
    }
}


.final-title {

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 50px;

    color: white;

    text-shadow:
        0 5px 20px rgba(0,0,0,.3);
}


.final-text {

    font-size: 22px;

    color: #ffe8f2;

    margin-top: 10px;
}


/* =========================================
   SMALL SPARKLES
========================================= */

.sparkle {

    position: absolute;

    width: 3px;

    height: 3px;

    background: white;

    border-radius: 50%;

    opacity: .5;

    animation:
        sparkle 2.5s infinite alternate;
}


@keyframes sparkle {

    from {
        opacity: .15;
        transform: scale(.6);
    }

    to {
        opacity: .9;
        transform: scale(1.5);
    }
}


/* =========================================
   MOBILE
========================================= */

@media (max-width: 600px) {

    .page {

        height: 850px;

        padding:
            18px 12px;
    }

    .intro-title {

        font-size: 31px;
    }

    .title {

        font-size: 34px;
    }

    .subtitle {

        font-size: 18px;
    }

    .tree-area {

        transform:
            scale(.78);

        margin:
            -25px auto;
    }

    .cake-area {

        transform:
            scale(.78);

        margin:
            -25px auto;
    }

    .balloon-area {

        height: 280px;
    }

    .balloon {

        width: 50px;

        height: 65px;
    }

    .balloon::after {

        top: 62px;
    }

    .balloon-message {

        font-size: 19px;
    }

    .card {

        width: 145px;
    }

    .card img,
    .missing {

        height: 180px;
    }

    .caption {

        font-size: 15px;
    }

    .final-title {

        font-size: 36px;
    }

    .letter {

        font-size: 17px;

        padding: 20px;
    }
}

</style>

</head>


<body>


<!-- =====================================
     PAGE 1
===================================== -->

<div class="page active" id="page1">

    <div class="content">

        <div class="intro-small">
            A little surprise...
        </div>

        <div class="intro-title">
            For Ricky
        </div>

        <div class="heart-box" id="start">

            <div class="arrow"></div>

            <div class="css-heart"></div>

        </div>

        <div class="subtitle">
            Press the arrow
        </div>

    </div>

</div>


<!-- FLASH -->

<div class="pink-flash" id="pinkFlash"></div>

<div class="burst" id="burst"></div>


<!-- =====================================
     PAGE 2
===================================== -->

<div class="page" id="page2">

    <div class="content">

        <div class="eyebrow">
            First things first
        </div>

        <div class="tree-area">

            <div class="trunk"></div>

            <div class="branch one"></div>
            <div class="branch two"></div>
            <div class="branch three"></div>

            <div class="leaf l1"></div>
            <div class="leaf l2"></div>
            <div class="leaf l3"></div>
            <div class="leaf l4"></div>
            <div class="leaf l5"></div>
            <div class="leaf l6"></div>
            <div class="leaf l7"></div>
            <div class="leaf l8"></div>
            <div class="leaf l9"></div>

        </div>

        <div class="title">
            A little tree<br>
            full of love
        </div>

        <button id="next2">
            Next
        </button>

    </div>

</div>


<!-- =====================================
     PAGE 3
===================================== -->

<div class="page" id="page3">

    <div class="content">

        <div class="eyebrow">
            Something special is coming...
        </div>

        <div class="cake-area" id="cakeArea">

            <div class="candle">
                <div class="flame"></div>
            </div>

            <div class="layer layer1"></div>

            <div class="cream cream1"></div>

            <div class="layer layer2"></div>

            <div class="cream cream2"></div>

            <div class="layer layer3"></div>

        </div>

        <div class="birthday-reveal">

            <div class="title">
                HAPPY BIRTHDAY
            </div>

            <div class="title">
                RICKY
            </div>

        </div>

        <button id="next3">
            Continue
        </button>

    </div>

</div>


<!-- =====================================
     PAGE 4
===================================== -->

<div class="page" id="page4">

    <div class="content">

        <div class="eyebrow">
            Pop the balloons
        </div>

        <div class="subtitle">
            Each one has something for you
        </div>

        <div class="balloon-area">

            <div class="balloon b1"
                 data-message="One of my favourite things about you is your smile.">
            </div>

            <div class="balloon b2"
                 data-message="I hope you always have reasons to smile.">
            </div>

            <div class="balloon b3"
                 data-message="You deserve all the beautiful moments coming your way.">
            </div>

            <div class="balloon b4"
                 data-message="Keep being the wonderful person you are.">
            </div>

            <div class="balloon-message"
                 id="balloonMessage">
            </div>

        </div>

        <button id="next4">
            See the pictures
        </button>

    </div>

</div>


<!-- =====================================
     PAGE 5
===================================== -->

<div class="page" id="page5">

    <div class="content">

        <div class="eyebrow">
            A walk down memory lane
        </div>

        <div class="title">
            Pictures I love
        </div>

        <div class="photos">

            <div class="card">

                __PHOTO1__

                <div class="caption">
                    One of my favourite pictures of you
                </div>

            </div>


            <div class="card">

                __PHOTO2__

                <div class="caption">
                    A moment I really love
                </div>

            </div>


            <div class="card">

                __PHOTO3__

                <div class="caption">
                    A picture that always makes me smile
                </div>

            </div>

        </div>

        <button id="next5">
            One last thing
        </button>

    </div>

</div>


<!-- =====================================
     PAGE 6
===================================== -->

<div class="page" id="page6">

    <div class="content">

        <div class="eyebrow">
            One last thing...
        </div>

        <div class="title">
            Something is waiting for you
        </div>

        <div class="envelope-stage">

            <div class="envelope" id="envelope">

                <div class="envelope-label">
                    For Ricky
                </div>

            </div>

        </div>

        <div class="subtitle" id="envelopeText">
            Wait for it...
        </div>

        <div class="letter" id="letter">

            <h2>
                Happy Birthday, Ricky
            </h2>

            <p>
                I hope this new year of your life
                brings you lots of happiness,
                beautiful memories and success.
            </p>

            <p>
                Keep smiling, keep dreaming and
                keep being the wonderful person
                you are.
            </p>

            <p>
                May every little wish of yours
                find its way to you.
            </p>

            <p>
                Wishing you the happiest birthday.
            </p>

            <button id="finalButton">
                Final Surprise
            </button>

        </div>

    </div>

</div>


<!-- =====================================
     PAGE 7
===================================== -->

<div class="page" id="page7">

    <div class="content">

        <div class="final-heart"></div>

        <div class="final-title">
            HAPPY BIRTHDAY RICKY
        </div>

        <div class="final-text">
            Hope your day is as special as you are.
        </div>

    </div>

</div>


<!-- MUSIC -->

<audio id="music" loop>

    <source
        src="data:audio/mpeg;base64,__SONG__"
        type="audio/mpeg">

</audio>


<script>


/* =========================================
   PAGE CONTROL
========================================= */

function showPage(number) {

    document
        .querySelectorAll(".page")
        .forEach(function(page) {

            page.classList.remove("active");

        });

    document
        .getElementById("page" + number)
        .classList.add("active");
}


/* =========================================
   MUSIC
========================================= */

var music =
    document.getElementById("music");


/* =========================================
   START HEART
========================================= */

document
    .getElementById("start")
    .addEventListener("click", function() {

        music.play().catch(function() {});


        var burst =
            document.getElementById("burst");

        var flash =
            document.getElementById("pinkFlash");


        /* Create pink burst particles */

        for (var i = 0; i < 55; i++) {

            var piece =
                document.createElement("div");

            piece.className =
                "burst-piece";

            var angle =
                Math.random() * Math.PI * 2;

            var distance =
                120 + Math.random() * 500;

            var x =
                Math.cos(angle) * distance;

            var y =
                Math.sin(angle) * distance;


            piece.style.setProperty(
                "--x",
                x + "px"
            );

            piece.style.setProperty(
                "--y",
                y + "px"
            );


            piece.style.width =
                (5 + Math.random() * 10) + "px";

            piece.style.height =
                (5 + Math.random() * 10) + "px";


            burst.appendChild(piece);
        }


        burst.style.display =
            "block";


        flash.classList.add("active");


        setTimeout(function() {

            burst.innerHTML = "";

            burst.style.display =
                "none";

        }, 1400);


        setTimeout(function() {

            showPage(2);

        }, 1100);

    });


/* =========================================
   TREE PAGE
========================================= */

document
    .getElementById("next2")
    .addEventListener("click", function() {

        showPage(3);

        var cake =
            document.getElementById("cakeArea");

        cake.classList.add("show");

    });


/* =========================================
   CAKE PAGE
========================================= */

document
    .getElementById("next3")
    .addEventListener("click", function() {

        showPage(4);

    });


/* =========================================
   BALLOONS
========================================= */

var balloons =
    document.querySelectorAll(".balloon");

var balloonMessage =
    document.getElementById("balloonMessage");


balloons.forEach(function(balloon) {

    balloon.addEventListener("click", function() {

        if (
            balloon.classList.contains("popped")
        ) {
            return;
        }


        var message =
            balloon.getAttribute(
                "data-message"
            );


        balloon.classList.add("popped");


        setTimeout(function() {

            balloonMessage.innerText =
                message;

            balloonMessage.classList.add(
                "show"
            );

        }, 250);

    });

});


document
    .getElementById("next4")
    .addEventListener("click", function() {

        showPage(5);

    });


/* =========================================
   PHOTOS
========================================= */

document
    .getElementById("next5")
    .addEventListener("click", function() {

        showPage(6);


        setTimeout(function() {

            document
                .getElementById("envelope")
                .classList.add("center");

        }, 150);

    });


/* =========================================
   ENVELOPE
========================================= */

document
    .getElementById("envelope")
    .addEventListener("click", function() {

        document
            .getElementById("envelope")
            .style.display = "none";


        document
            .getElementById("envelopeText")
            .style.display = "none";


        document
            .getElementById("letter")
            .classList.add("show");

    });


/* =========================================
   FINAL
========================================= */

document
    .getElementById("finalButton")
    .addEventListener("click", function() {

        showPage(7);

        createParticles();

    });


/* =========================================
   FINAL PARTICLES
========================================= */

function createParticles() {

    for (var i = 0; i < 100; i++) {

        var particle =
            document.createElement("div");


        particle.style.position =
            "fixed";

        particle.style.left =
            Math.random() * 100 + "%";

        particle.style.top =
            "-20px";

        particle.style.width =
            (4 + Math.random() * 8) + "px";

        particle.style.height =
            (4 + Math.random() * 8) + "px";

        particle.style.borderRadius =
            "50%";

        particle.style.background =
            "#f48ab8";

        particle.style.zIndex =
            "99999";


        document.body.appendChild(
            particle
        );


        var duration =
            2500 +
            Math.random() * 3000;


        particle.animate(

            [
                {
                    transform:
                        "translateY(0) rotate(0deg)",

                    opacity: 1
                },

                {
                    transform:
                        "translateY(100vh) rotate(720deg)",

                    opacity: 0.2
                }
            ],

            {
                duration:
                    duration,

                easing:
                    "linear"
            }

        );


        setTimeout(
            function(el) {

                return function() {

                    el.remove();

                };

            }(particle),

            duration
        );

    }

}


/* =========================================
   BACKGROUND SPARKLES
========================================= */

function createSparkles() {

    var pages =
        document.querySelectorAll(".page");


    pages.forEach(function(page) {

        for (var i = 0; i < 30; i++) {

            var sparkle =
                document.createElement("div");


            sparkle.className =
                "sparkle";


            sparkle.style.left =
                Math.random() * 100 + "%";


            sparkle.style.top =
                Math.random() * 100 + "%";


            sparkle.style.animationDelay =
                Math.random() * 3 + "s";


            page.appendChild(
                sparkle
            );

        }

    });

}


createSparkles();


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

    return (
        '<div class="missing">'
        'Photo not found'
        '</div>'
    )


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
