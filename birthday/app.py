import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------

st.set_page_config(
    page_title="A Surprise for Ricky",
    page_icon="♥",
    layout="wide"
)

# ---------------------------------------------------------
# LOAD ASSETS
# ---------------------------------------------------------

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"


def image_to_base64(filename):
    path = ASSETS_DIR / filename

    if not path.exists():
        return ""

    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


photo1 = image_to_base64("photo1.jpeg")
photo2 = image_to_base64("photo2.jpeg")
photo3 = image_to_base64("photo3.jpeg")


# ---------------------------------------------------------
# HTML
# ---------------------------------------------------------

html = r"""
<!DOCTYPE html>
<html>

<head>

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Delius&display=swap"
      rel="stylesheet">

<style>

/* =====================================================
   RESET
===================================================== */

* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
}

body {
    font-family: "Patrick Hand", cursive;
}


/* =====================================================
   MAIN BACKGROUND
   VIDEO STYLE PURPLE GLOW
===================================================== */

.app {

    width: 100%;
    height: 100vh;
    min-height: 700px;

    position: relative;
    overflow: hidden;

    background:

        radial-gradient(
            circle at 50% 38%,
            rgba(236, 126, 205, 0.62) 0%,
            rgba(163, 48, 157, 0.45) 22%,
            rgba(88, 20, 91, 0.25) 48%,
            transparent 72%
        ),

        radial-gradient(
            circle at 18% 15%,
            rgba(221, 108, 207, 0.30),
            transparent 35%
        ),

        radial-gradient(
            circle at 82% 75%,
            rgba(154, 54, 159, 0.32),
            transparent 40%
        ),

        linear-gradient(
            180deg,
            #7b2878 0%,
            #641b65 35%,
            #40103f 72%,
            #210921 100%
        );

    color: white;
}


/* =====================================================
   SOFT GLOW
===================================================== */

.app:before {

    content: "";

    position: absolute;

    width: 500px;
    height: 500px;

    left: 50%;
    top: 42%;

    transform: translate(-50%, -50%);

    background:
        radial-gradient(
            circle,
            rgba(255, 180, 229, 0.20),
            transparent 68%
        );

    filter: blur(20px);

    pointer-events: none;

    animation: backgroundGlow 4s ease-in-out infinite alternate;
}

@keyframes backgroundGlow {

    from {
        opacity: 0.65;
        transform:
            translate(-50%, -50%)
            scale(0.9);
    }

    to {
        opacity: 1;
        transform:
            translate(-50%, -50%)
            scale(1.15);
    }
}


/* =====================================================
   MOVING SPARKLES
===================================================== */

.sparkle {

    position: absolute;

    width: 3px;
    height: 3px;

    border-radius: 50%;

    background: #fff;

    box-shadow:
        0 0 5px #fff,
        0 0 12px rgba(255,190,235,0.9);

    pointer-events: none;

    animation:
        sparkleMove
        var(--duration)
        ease-in-out
        infinite;

    animation-delay: var(--delay);

    opacity: 0.2;
}

.sparkle.big {

    width: 5px;
    height: 5px;

    box-shadow:
        0 0 7px #fff,
        0 0 17px rgba(255,180,235,1);
}


@keyframes sparkleMove {

    0% {

        transform:
            translate(0, 0)
            scale(0.4);

        opacity: 0.1;
    }

    25% {
        opacity: 0.9;
    }

    50% {

        transform:
            translate(
                var(--moveX),
                var(--moveY)
            )
            scale(1.5);

        opacity: 1;
    }

    75% {
        opacity: 0.5;
    }

    100% {

        transform:
            translate(
                calc(var(--moveX) * -0.7),
                calc(var(--moveY) * -0.5)
            )
            scale(0.4);

        opacity: 0.1;
    }
}


/* =====================================================
   PAGE SYSTEM
===================================================== */

.page {

    position: absolute;

    inset: 0;

    display: none;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    padding: 25px;

    text-align: center;

    z-index: 10;
}

.page.active {
    display: flex;
}


/* =====================================================
   TEXT
===================================================== */

.small-title {

    font-size: 21px;

    letter-spacing: 1px;

    margin-bottom: 24px;

    color: #fff7fc;
}

.big-title {

    font-family: "Delius", cursive;

    font-size: 43px;

    line-height: 1.15;

    color: white;

    text-shadow:
        0 3px 12px rgba(0,0,0,0.25);
}

.sub-title {

    font-size: 22px;

    margin-top: 8px;

    color: #ffeaf6;
}


/* =====================================================
   BUTTON
===================================================== */

.next-btn {

    margin-top: 22px;

    border: none;
    outline: none;

    padding: 9px 27px;

    border-radius: 30px;

    background:
        linear-gradient(
            180deg,
            #f5afd2,
            #dc80b1
        );

    color: white;

    font-family: "Patrick Hand", cursive;

    font-size: 20px;

    cursor: pointer;

    box-shadow:
        0 5px 18px rgba(0,0,0,0.25);

    transition: 0.25s;
}

.next-btn:hover {
    transform: scale(1.07);
}


/* =====================================================
   PAGE 1 - HEART + ARROW
===================================================== */

.first-heart-area {

    position: relative;

    width: 300px;
    height: 280px;

    margin-top: 5px;
}


.start-heart {

    position: absolute;

    width: 100px;
    height: 100px;

    left: 100px;
    top: 85px;

    background: #ffd8e9;

    transform: rotate(-45deg);

    border-radius: 12px;

    box-shadow:
        0 0 25px rgba(255,190,220,0.7),
        0 0 55px rgba(255,130,210,0.35);

    cursor: pointer;

    z-index: 5;

    transition: 0.2s;
}

.start-heart:before,
.start-heart:after {

    content: "";

    position: absolute;

    width: 100px;
    height: 100px;

    background: #ffd8e9;

    border-radius: 50%;
}

.start-heart:before {
    top: -50px;
    left: 0;
}

.start-heart:after {
    top: 0;
    left: 50px;
}


/* =====================================================
   ARROW - STARTING CORNER
===================================================== */

.arrow {

    position: absolute;

    width: 135px;
    height: 6px;

    background: #f3bfd9;

    left: 5px;
    bottom: 38px;

    transform:
        rotate(-25deg);

    transform-origin: left center;

    border-radius: 10px;

    z-index: 10;

    cursor: pointer;

    animation:
        arrowMove
        1.2s
        ease-in-out
        infinite alternate;
}

.arrow:after {

    content: "";

    position: absolute;

    right: -3px;
    top: -7px;

    border-left:
        19px solid #f3bfd9;

    border-top:
        10px solid transparent;

    border-bottom:
        10px solid transparent;
}

@keyframes arrowMove {

    from {
        transform:
            rotate(-25deg)
            translateX(0);
    }

    to {
        transform:
            rotate(-25deg)
            translateX(8px);
    }
}


/* =====================================================
   HEART BLAST
===================================================== */

.blast-heart {

    animation:
        heartBlast
        0.6s
        forwards;
}

@keyframes heartBlast {

    0% {
        transform:
            rotate(-45deg)
            scale(1);
        opacity: 1;
    }

    45% {
        transform:
            rotate(-45deg)
            scale(1.45);
        opacity: 0.9;
    }

    100% {
        transform:
            rotate(-45deg)
            scale(0);
        opacity: 0;
    }
}


/* =====================================================
   PINK SPREAD
===================================================== */

.pink-flash {

    position: fixed;

    inset: 0;

    background:
        radial-gradient(
            circle,
            #ffd3e8 0%,
            #f49bc5 35%,
            #b64b9e 100%
        );

    opacity: 0;

    pointer-events: none;

    z-index: 1000;
}

.pink-flash.show {

    animation:
        pinkSpread
        1.1s
        forwards;
}

@keyframes pinkSpread {

    0% {
        opacity: 0;
        transform: scale(0.1);
    }

    35% {
        opacity: 0.98;
        transform: scale(1.1);
    }

    100% {
        opacity: 0;
        transform: scale(1.5);
    }
}


/* =====================================================
   PARTICLES
===================================================== */

.particle {

    position: fixed;

    width: 7px;
    height: 7px;

    border-radius: 50%;

    background: #ffd6e9;

    pointer-events: none;

    z-index: 3000;

    animation:
        particleFly
        1.2s
        ease-out
        forwards;
}

@keyframes particleFly {

    0% {

        transform:
            translate(0,0)
            scale(1);

        opacity: 1;
    }

    100% {

        transform:
            translate(
                var(--x),
                var(--y)
            )
            rotate(360deg)
            scale(0.1);

        opacity: 0;
    }
}


/* =====================================================
   PAGE 2 - CAKE
===================================================== */

.cake-area {

    position: relative;

    width: 330px;
    height: 410px;

    margin-top: -20px;
}

.plate {

    position: absolute;

    width: 250px;
    height: 20px;

    bottom: 30px;
    left: 40px;

    border-radius: 50%;

    background: rgba(255,255,255,0.85);

    box-shadow:
        0 5px 12px rgba(0,0,0,0.25);
}

.cake-layer {

    position: absolute;

    left: 50%;

    transform:
        translateX(-50%);

    border-radius: 9px;

    background:
        linear-gradient(
            180deg,
            #f6b1d1,
            #db79ad
        );

    box-shadow:
        0 7px 13px rgba(0,0,0,0.25);

    opacity: 0;
}

.layer3 {

    height: 67px;
    bottom: 47px;
    width: 230px;
}

.layer2 {

    height: 62px;
    bottom: 105px;
    width: 195px;
}

.layer1 {

    height: 55px;
    bottom: 158px;
    width: 155px;
}

.cream {

    position: absolute;

    left: 50%;

    transform:
        translateX(-50%);

    height: 14px;

    border-radius: 50%;

    background: #fff9fc;

    opacity: 0;

    z-index: 4;
}

.cream1 {
    bottom: 153px;
    width: 145px;
}

.cream2 {
    bottom: 100px;
    width: 184px;
}

.cream3 {
    bottom: 43px;
    width: 220px;
}

.candle {

    position: absolute;

    width: 19px;
    height: 75px;

    left: 50%;

    bottom: 213px;

    transform:
        translateX(-50%);

    background:
        repeating-linear-gradient(
            -45deg,
            #fff,
            #fff 8px,
            #f2a5c8 8px,
            #f2a5c8 16px
        );

    border-radius: 5px;

    opacity: 0;

    z-index: 6;
}

.flame {

    position: absolute;

    width: 18px;
    height: 28px;

    left: 50%;

    bottom: 283px;

    transform:
        translateX(-50%)
        rotate(45deg);

    background: #ffe79c;

    border-radius:
        50% 50% 50% 0;

    opacity: 0;

    box-shadow:
        0 0 16px #ffd67b;

    z-index: 7;
}


/* =====================================================
   CAKE ANIMATION
===================================================== */

.cake-area.build .layer3 {
    animation:
        layerDrop
        0.65s
        0.2s
        forwards;
}

.cake-area.build .layer2 {
    animation:
        layerDrop
        0.65s
        0.9s
        forwards;
}

.cake-area.build .layer1 {
    animation:
        layerDrop
        0.65s
        1.6s
        forwards;
}

.cake-area.build .cream1 {
    animation:
        creamAppear
        0.45s
        2.15s
        forwards;
}

.cake-area.build .cream2 {
    animation:
        creamAppear
        0.45s
        2.45s
        forwards;
}

.cake-area.build .cream3 {
    animation:
        creamAppear
        0.45s
        2.75s
        forwards;
}

.cake-area.build .candle {
    animation:
        candleDrop
        0.7s
        3.1s
        forwards;
}

.cake-area.build .flame {
    animation:
        flameDrop
        0.6s
        3.55s
        forwards,
        flicker
        0.8s
        4.15s
        infinite
        alternate;
}

@keyframes layerDrop {

    0% {
        transform:
            translate(-50%, -280px)
            scale(0.9);
        opacity: 0;
    }

    70% {
        transform:
            translate(-50%, 10px)
            scale(1.03);
        opacity: 1;
    }

    100% {
        transform:
            translate(-50%, 0)
            scale(1);
        opacity: 1;
    }
}

@keyframes creamAppear {

    from {
        opacity: 0;
        transform:
            translateX(-50%)
            scaleX(0.4);
    }

    to {
        opacity: 1;
        transform:
            translateX(-50%)
            scaleX(1);
    }
}

@keyframes candleDrop {

    0% {
        opacity: 0;
        transform:
            translate(-50%, -180px)
            rotate(-10deg);
    }

    75% {
        transform:
            translate(-50%, 8px)
            rotate(4deg);
    }

    100% {
        opacity: 1;
        transform:
            translate(-50%, 0)
            rotate(0);
    }
}

@keyframes flameDrop {

    0% {
        opacity: 0;
        transform:
            translate(-50%, -150px)
            rotate(45deg);
    }

    100% {
        opacity: 1;
        transform:
            translate(-50%, 0)
            rotate(45deg);
    }
}

@keyframes flicker {

    from {
        transform:
            translateX(-50%)
            rotate(42deg)
            scale(0.9);
    }

    to {
        transform:
            translateX(-50%)
            rotate(48deg)
            scale(1.05);
    }
}


/* =====================================================
   HAPPY BIRTHDAY - BELOW CAKE
===================================================== */

.cake-message {

    position: absolute;

    left: 50%;

    bottom: -25px;

    transform:
        translateX(-50%);

    width: 100%;

    font-family:
        "Delius",
        cursive;

    font-size: 34px;

    line-height: 1.15;

    color: white;

    opacity: 0;
}

.cake-message.show {

    animation:
        messageAppear
        1s
        4s
        forwards;
}

@keyframes messageAppear {

    from {
        opacity: 0;
        transform:
            translateX(-50%)
            translateY(20px);
    }

    to {
        opacity: 1;
        transform:
            translateX(-50%)
            translateY(0);
    }
}


/* =====================================================
   PAGE 3 - BALLOONS
===================================================== */

.balloon-title {

    font-size: 25px;

    margin-bottom: 20px;
}

.balloon-area {

    width: 360px;
    height: 365px;

    position: relative;
}

.balloon {

    position: absolute;

    width: 75px;
    height: 95px;

    border-radius:
        50% 50% 45% 45%;

    cursor: pointer;

    transition: 0.15s;

    box-shadow:
        inset -12px -9px 18px rgba(0,0,0,0.13),
        inset 8px 5px 10px rgba(255,255,255,0.25);

    z-index: 4;
}

.balloon:after {

    content: "";

    position: absolute;

    width: 2px;
    height: 95px;

    background:
        rgba(255,255,255,0.65);

    top: 93px;
    left: 50%;
}

.balloon:before {

    content: "";

    position: absolute;

    bottom: -7px;
    left: 50%;

    transform:
        translateX(-50%);

    width: 0;
    height: 0;

    border-left:
        6px solid transparent;

    border-right:
        6px solid transparent;

    border-top:
        10px solid currentColor;
}

.b1 {
    left: 35px;
    top: 45px;
    background: #f6a4c7;
    color: #f6a4c7;
}

.b2 {
    left: 135px;
    top: 5px;
    background: #e9b0df;
    color: #e9b0df;
}

.b3 {
    left: 235px;
    top: 48px;
    background: #a9c3dc;
    color: #a9c3dc;
}

.b4 {
    left: 135px;
    top: 130px;
    background: #f3c0dc;
    color: #f3c0dc;
}

.balloon:hover {
    transform:
        translateY(-5px)
        scale(1.05);
}

.balloon.popped {

    animation:
        popBalloon
        0.35s
        forwards;
}

@keyframes popBalloon {

    0% {
        transform: scale(1);
        opacity: 1;
    }

    50% {
        transform: scale(1.35);
        opacity: 0.8;
    }

    100% {
        transform: scale(0);
        opacity: 0;
    }
}


/* =====================================================
   TRANSPARENT PINK MESSAGE BOX
===================================================== */

.balloon-message {

    position: absolute;

    width: 320px;

    left: 50%;
    bottom: 5px;

    transform:
        translateX(-50%)
        translateY(20px);

    padding: 14px 18px;

    border-radius: 18px;

    background:
        rgba(245,158,198,0.30);

    border:
        1px solid
        rgba(255,224,241,0.45);

    box-shadow:
        0 6px 20px rgba(0,0,0,0.14);

    backdrop-filter:
        blur(5px);

    -webkit-backdrop-filter:
        blur(5px);

    font-size: 21px;

    line-height: 1.2;

    color: #fff8fc;

    opacity: 0;

    transition:
        0.45s ease;
}

.balloon-message.show {

    opacity: 1;

    transform:
        translateX(-50%)
        translateY(0);
}


/* =====================================================
   PAGE 4 - PHOTOS
===================================================== */

.memory-title {

    font-size: 25px;

    margin-bottom: 25px;
}

.photo-container {

    display: flex;

    justify-content: center;
    align-items: center;

    gap: 20px;

    width: 100%;
    max-width: 900px;
}

.photo-card {

    width: 230px;

    padding:
        9px 9px 16px;

    background: white;

    border-radius: 4px;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.25);

    transform:
        rotate(-2deg);

    transition: 0.3s;
}

.photo-card:nth-child(2) {
    transform: rotate(2deg);
}

.photo-card:nth-child(3) {
    transform: rotate(-1deg);
}

.photo-card:hover {

    transform:
        rotate(0deg)
        translateY(-8px);
}

.photo-card img {

    display: block;

    width: 100%;

    height: 230px;

    object-fit: cover;

    border-radius: 2px;
}

.photo-caption {

    color: #562047;

    font-size: 20px;

    margin-top: 10px;

    line-height: 1.1;
}


/* =====================================================
   PAGE 5 - ENVELOPE
===================================================== */

.envelope-page {
    perspective: 1000px;
}

.envelope {

    position: relative;

    width: 290px;
    height: 190px;

    cursor: pointer;

    animation:
        envelopeFromSide
        1.3s
        ease-out
        forwards;

    filter:
        drop-shadow(
            0 15px 25px rgba(0,0,0,0.25)
        );
}

@keyframes envelopeFromSide {

    0% {
        transform:
            translateX(-120vw)
            rotate(-5deg);
    }

    70% {
        transform:
            translateX(25px)
            rotate(2deg);
    }

    100% {
        transform:
            translateX(0)
            rotate(0);
    }
}

.envelope-back {

    position: absolute;

    inset: 0;

    background:
        #f7c8dc;

    border-radius: 7px;

    box-shadow:
        inset 0 0 20px rgba(120,30,80,0.12);
}

.envelope-front {

    position: absolute;

    left: 0;
    right: 0;
    bottom: 0;

    height: 125px;

    background:
        #efafd0;

    clip-path:
        polygon(
            0 0,
            50% 58%,
            100% 0,
            100% 100%,
            0 100%
        );

    border-radius: 0 0 7px 7px;

    z-index: 3;
}

.envelope-flap {

    position: absolute;

    top: 0;
    left: 0;

    width: 100%;
    height: 125px;

    background:
        #ffd9e8;

    clip-path:
        polygon(
            0 0,
            100% 0,
            50% 72%
        );

    transform-origin: top center;

    z-index: 5;

    transition:
        transform 0.7s ease;
}

.envelope-heart {

    position: absolute;

    z-index: 8;

    left: 50%;
    top: 74px;

    transform:
        translateX(-50%);

    font-size: 29px;

    color: #d65a96;
}

.envelope-hint {

    margin-top: 25px;

    font-size: 21px;

    color: #ffeaf6;
}


/* =====================================================
   FULL LETTER
===================================================== */

.letter-page {

    justify-content: center;

    padding: 25px;

    opacity: 0;

    transform:
        scale(0.85);

    transition:
        opacity 0.7s ease,
        transform 0.7s ease;
}

.letter-page.open {

    opacity: 1;

    transform:
        scale(1);
}

.letter-paper {

    width: min(680px, 90vw);

    max-height: 78vh;

    overflow-y: auto;

    padding:
        38px 42px;

    background:
        linear-gradient(
            180deg,
            #fffaf5,
            #fff4f7
        );

    border-radius: 6px;

    box-shadow:
        0 20px 50px
        rgba(0,0,0,0.35);

    color: #542044;

    text-align: left;

    position: relative;

    animation:
        letterOpen
        0.8s
        ease-out;
}

@keyframes letterOpen {

    from {
        transform:
            translateY(40px)
            scale(0.85);
        opacity: 0;
    }

    to {
        transform:
            translateY(0)
            scale(1);
        opacity: 1;
    }
}

.letter-to {

    font-family:
        "Delius",
        cursive;

    font-size: 30px;

    margin-bottom: 22px;

    color: #7b285f;
}

.letter-text {

    font-size: 21px;

    line-height: 1.55;

    white-space: pre-line;
}

.letter-sign {

    margin-top: 28px;

    text-align: right;

    font-family:
        "Delius",
        cursive;

    font-size: 27px;

    color: #8a356c;
}


/* =====================================================
   FINAL FROM MAGGI
===================================================== */

.from-page {

    text-align: center;
}

.from-title {

    font-family:
        "Delius",
        cursive;

    font-size: 48px;

    color: #fff;

    text-shadow:
        0 4px 15px rgba(0,0,0,0.3);
}

.from-sub {

    font-size: 25px;

    color: #ffe8f4;

    margin-top: 10px;
}


/* =====================================================
   FINAL
===================================================== */

.final-heart {

    position: relative;

    width: 105px;
    height: 105px;

    background: #f4a1c8;

    transform:
        rotate(-45deg);

    border-radius: 12px;

    box-shadow:
        0 0 35px rgba(255,170,215,0.65);

    margin-bottom: 45px;
}

.final-heart:before,
.final-heart:after {

    content: "";

    position: absolute;

    width: 105px;
    height: 105px;

    background: #f4a1c8;

    border-radius: 50%;
}

.final-heart:before {
    top: -52px;
    left: 0;
}

.final-heart:after {
    top: 0;
    left: 52px;
}

.final-title {

    font-family:
        "Delius",
        cursive;

    font-size: 48px;

    color: white;
}

.final-name {

    font-size: 30px;

    color: #ffe3f1;

    margin-top: 8px;
}


/* =====================================================
   MOBILE
===================================================== */

@media (max-width: 700px) {

    .big-title {
        font-size: 34px;
    }

    .photo-container {
        gap: 8px;
    }

    .photo-card {
        width: 30vw;
        max-width: 180px;
    }

    .photo-card img {
        height: 30vw;
        max-height: 180px;
    }

    .photo-caption {
        font-size: 16px;
    }

    .letter-paper {
        padding: 28px 24px;
    }

    .letter-text {
        font-size: 19px;
    }

    .from-title,
    .final-title {
        font-size: 38px;
    }
}

</style>
</head>


<body>

<div class="app">


<!-- =====================================================
     MOVING SPARKLES
===================================================== -->

<span class="sparkle big"
style="left:8%;top:13%;--moveX:25px;--moveY:35px;--duration:4s;--delay:0s;"></span>

<span class="sparkle"
style="left:18%;top:28%;--moveX:-30px;--moveY:45px;--duration:5s;--delay:1s;"></span>

<span class="sparkle big"
style="left:30%;top:8%;--moveX:35px;--moveY:30px;--duration:4.5s;--delay:0.5s;"></span>

<span class="sparkle"
style="left:44%;top:20%;--moveX:-25px;--moveY:35px;--duration:5.5s;--delay:1.5s;"></span>

<span class="sparkle big"
style="left:57%;top:10%;--moveX:30px;--moveY:40px;--duration:4.2s;--delay:0.8s;"></span>

<span class="sparkle"
style="left:72%;top:25%;--moveX:-35px;--moveY:30px;--duration:5s;--delay:2s;"></span>

<span class="sparkle big"
style="left:88%;top:15%;--moveX:25px;--moveY:45px;--duration:4.8s;--delay:0.2s;"></span>

<span class="sparkle"
style="left:10%;top:55%;--moveX:30px;--moveY:-35px;--duration:5.2s;--delay:1.2s;"></span>

<span class="sparkle big"
style="left:25%;top:70%;--moveX:-25px;--moveY:-40px;--duration:4.3s;--delay:2.2s;"></span>

<span class="sparkle"
style="left:40%;top:82%;--moveX:35px;--moveY:-30px;--duration:5.5s;--delay:0.7s;"></span>

<span class="sparkle big"
style="left:63%;top:75%;--moveX:-30px;--moveY:-40px;--duration:4.6s;--delay:1.7s;"></span>

<span class="sparkle"
style="left:80%;top:62%;--moveX:25px;--moveY:-35px;--duration:5s;--delay:0.4s;"></span>

<span class="sparkle big"
style="left:92%;top:83%;--moveX:-25px;--moveY:-30px;--duration:4.7s;--delay:1.4s;"></span>


<!-- =====================================================
     PAGE 1
===================================================== -->

<section class="page active" id="page1">

    <div class="small-title">
        First things first
    </div>

    <div class="first-heart-area">

        <div
            class="start-heart"
            id="startHeart">
        </div>

        <div
            class="arrow"
            id="startArrow">
        </div>

    </div>

    <div class="sub-title">
        Something special is waiting...
    </div>

</section>


<!-- =====================================================
     PAGE 2 - CAKE
===================================================== -->

<section class="page" id="page2">

    <div class="cake-area" id="cakeArea">

        <div class="plate"></div>

        <div class="cake-layer layer3"></div>
        <div class="cake-layer layer2"></div>
        <div class="cake-layer layer1"></div>

        <div class="cream cream1"></div>
        <div class="cream cream2"></div>
        <div class="cream cream3"></div>

        <div class="candle"></div>
        <div class="flame"></div>

        <div class="cake-message" id="cakeMessage">
            Happy Birthday Ricky!
        </div>

    </div>

    <button
        class="next-btn"
        id="cakeNext"
        style="display:none;">
        Next
    </button>

</section>


<!-- =====================================================
     PAGE 3 - BALLOONS
===================================================== -->

<section class="page" id="page3">

    <div class="balloon-title">
        Pop the balloons
    </div>

    <div class="balloon-area">

        <div class="balloon b1"
             data-message="You make ordinary moments feel special.">
        </div>

        <div class="balloon b2"
             data-message="Somehow, you always make me smile.">
        </div>

        <div class="balloon b3"
             data-message="I am really grateful for every little moment.">
        </div>

        <div class="balloon b4"
             data-message="You are someone very special to me.">
        </div>

        <div
            class="balloon-message"
            id="balloonMessage">
        </div>

    </div>

    <button
        class="next-btn"
        id="balloonNext">
        Next
    </button>

</section>


<!-- =====================================================
     PAGE 4 - PHOTOS
===================================================== -->

<section class="page" id="page4">

    <div class="memory-title">
        A little collection of my favourite pictures of you
    </div>

    <div class="photo-container">

        <div class="photo-card">

            <img src="data:image/jpeg;base64,__PHOTO1__">

            <div class="photo-caption">
                One of my favourite pictures of you
            </div>

        </div>


        <div class="photo-card">

            <img src="data:image/jpeg;base64,__PHOTO2__">

            <div class="photo-caption">
                A moment I really love
            </div>

        </div>


        <div class="photo-card">

            <img src="data:image/jpeg;base64,__PHOTO3__">

            <div class="photo-caption">
                A picture that always makes me smile
            </div>

        </div>

    </div>

    <button
        class="next-btn"
        id="photoNext">
        Next
    </button>

</section>


<!-- =====================================================
     PAGE 5 - ENVELOPE
===================================================== -->

<section class="page envelope-page" id="page5">

    <div class="envelope"
         id="envelope">

        <div class="envelope-back"></div>

        <div class="envelope-flap"></div>

        <div class="envelope-front"></div>

        <div class="envelope-heart">
            ♥
        </div>

    </div>

    <div class="envelope-hint">
        A little something for you...
    </div>

</section>


<!-- =====================================================
     PAGE 6 - FULL LETTER
===================================================== -->

<section class="page letter-page" id="page6">

    <div class="letter-paper">

        <div class="letter-to">
            To my Ricky,
        </div>

        <div class="letter-text">
There are some people who quietly become very special without even trying.

You are one of those people to me.

I don't know how perfectly to put everything I feel into words, but I just want you to know that having you as a part of my life means more to me than I can explain.

I hope this birthday brings you lots of happiness, beautiful moments and everything your heart wishes for.

And whenever life gets busy, I hope you remember that there is someone who genuinely wishes the best for you and is always happy to see you smile.

Today is your special day, but somehow I feel lucky too — because I get to wish someone as special as you a Happy Birthday.

Keep smiling, keep being yourself, and keep making the world a little brighter just by being in it.

Happy Birthday, Ricky. ♥
        </div>

        <div class="letter-sign">
            With lots of love,<br>
            Your Maggi
        </div>

        <button
            class="next-btn"
            id="letterNext">
            Next
        </button>

    </div>

</section>


<!-- =====================================================
     PAGE 7 - FROM MAGGI
===================================================== -->

<section class="page from-page" id="page7">

    <div class="from-title">
        From your Maggi ♥
    </div>

    <div class="from-sub">
        To my very special Ricky
    </div>

    <button
        class="next-btn"
        id="finalNext">
        One last thing
    </button>

</section>


<!-- =====================================================
     PAGE 8 - FINAL
===================================================== -->

<section class="page" id="page8">

    <div class="final-heart"></div>

    <div class="final-title">
        HAPPY BIRTHDAY
    </div>

    <div class="final-name">
        Ricky!
    </div>

</section>


<div class="pink-flash"
     id="pinkFlash">
</div>


<div class="confetti-box"
     id="confettiBox">
</div>


<script>

/* =====================================================
   PAGE NAVIGATION
===================================================== */

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


/* =====================================================
   PAGE 1
   ARROW -> HEART -> BLAST
===================================================== */

const startHeart =
    document.getElementById("startHeart");

const startArrow =
    document.getElementById("startArrow");

const pinkFlash =
    document.getElementById("pinkFlash");


function startSurprise() {

    startHeart.classList.add("blast-heart");

    pinkFlash.classList.add("show");

    createHeartParticles();

    setTimeout(function() {

        showPage(2);

        const cake =
            document.getElementById("cakeArea");

        cake.classList.add("build");

        setTimeout(function() {

            document
                .getElementById("cakeMessage")
                .classList.add("show");

        }, 300);

    }, 850);
}


startArrow.addEventListener(
    "click",
    startSurprise
);

startHeart.addEventListener(
    "click",
    startSurprise
);


/* =====================================================
   HEART PARTICLES
===================================================== */

function createHeartParticles() {

    for (let i = 0; i < 28; i++) {

        const particle =
            document.createElement("div");

        particle.className =
            "particle";

        particle.innerHTML = "♥";

        particle.style.left =
            "50vw";

        particle.style.top =
            "45vh";

        particle.style.color =
            "#ffd5e8";

        particle.style.setProperty(
            "--x",
            (Math.random() * 500 - 250) + "px"
        );

        particle.style.setProperty(
            "--y",
            (Math.random() * 500 - 250) + "px"
        );

        document.body.appendChild(
            particle
        );

        setTimeout(function() {
            particle.remove();
        }, 1300);
    }
}


/* =====================================================
   CAKE NEXT
===================================================== */

setTimeout(function() {

    const cakeNext =
        document.getElementById("cakeNext");

    cakeNext.style.display = "inline-block";

}, 5200);


document
    .getElementById("cakeNext")
    .addEventListener(
        "click",
        function() {

            showPage(3);

        }
    );


/* =====================================================
   BALLOONS
===================================================== */

const balloons =
    document.querySelectorAll(".balloon");

const balloonMessage =
    document.getElementById("balloonMessage");


balloons.forEach(function(balloon) {

    balloon.addEventListener(
        "click",
        function() {

            if (
                balloon.classList.contains(
                    "popped"
                )
            ) {
                return;
            }

            balloon.classList.add(
                "popped"
            );

            balloonMessage.innerText =
                balloon.dataset.message;

            balloonMessage.classList.remove(
                "show"
            );

            setTimeout(function() {

                balloonMessage.classList.add(
                    "show"
                );

            }, 100);

        }
    );

});


document
    .getElementById("balloonNext")
    .addEventListener(
        "click",
        function() {

            showPage(4);

        }
    );


/* =====================================================
   PHOTOS NEXT
===================================================== */

document
    .getElementById("photoNext")
    .addEventListener(
        "click",
        function() {

            showPage(5);

        }
    );


/* =====================================================
   ENVELOPE
   CLICK -> FULL LETTER
===================================================== */

const envelope =
    document.getElementById("envelope");

envelope.addEventListener(
    "click",
    function() {

        envelope.style.transform =
            "scale(0.8)";

        envelope.style.opacity =
            "0";

        setTimeout(function() {

            showPage(6);

            const letter =
                document.getElementById("page6");

            letter.classList.add("open");

        }, 450);

    }
);


/* =====================================================
   LETTER NEXT
===================================================== */

document
    .getElementById("letterNext")
    .addEventListener(
        "click",
        function() {

            showPage(7);

        }
    );


/* =====================================================
   FROM MAGGI -> FINAL
===================================================== */

document
    .getElementById("finalNext")
    .addEventListener(
        "click",
        function() {

            showPage(8);

            createConfetti();

        }
    );


/* =====================================================
   CONFETTI
===================================================== */

function createConfetti() {

    const box =
        document.getElementById(
            "confettiBox"
        );

    box.innerHTML = "";

    for (let i = 0; i < 70; i++) {

        const piece =
            document.createElement("div");

        piece.className =
            "confetti";

        piece.style.left =
            Math.random() * 100 + "%";

        piece.style.animationDelay =
            Math.random() * 1.5 + "s";

        piece.style.transform =
            "rotate(" +
            Math.random() * 360 +
            "deg)";

        piece.style.background =
            [
                "#f7a8cc",
                "#ffd8e9",
                "#e8b4dd",
                "#b9c9e5",
                "#fff1c9"
            ][
                Math.floor(
                    Math.random() * 5
                )
            ];

        box.appendChild(piece);

    }
}

</script>

</div>

</body>
</html>
"""


# ---------------------------------------------------------
# INSERT PHOTOS
# ---------------------------------------------------------

html = html.replace("__PHOTO1__", photo1)
html = html.replace("__PHOTO2__", photo2)
html = html.replace("__PHOTO3__", photo3)


# ---------------------------------------------------------
# DISPLAY
# ---------------------------------------------------------

components.html(
    html,
    height=850,
    scrolling=False
)
"""


# ---------------------------------------------------------
# DISPLAY
# ---------------------------------------------------------

components.html(
    html,
    height=850,
    scrolling=False
)
