import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="A Surprise for Ricky",
    page_icon="♥",
    layout="wide"
)


# =========================================================
# LOAD ASSETS
# =========================================================

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


# =========================================================
# HTML
# =========================================================

html = r"""
<!DOCTYPE html>
<html>

<head>

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Delius&display=swap"
      rel="stylesheet">

<style>

/* =========================================================
   RESET
========================================================= */

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

    background: #32102f;
}


/* =========================================================
   MAIN BACKGROUND
========================================================= */

.app {

    width: 100%;
    height: 100vh;

    min-height: 700px;

    position: relative;

    overflow: hidden;

    color: white;

    background:

        radial-gradient(
            circle at 50% 20%,
            rgba(255,150,207,0.40),
            transparent 28%
        ),

        radial-gradient(
            circle at 15% 75%,
            rgba(191,104,189,0.35),
            transparent 30%
        ),

        radial-gradient(
            circle at 85% 70%,
            rgba(226,126,188,0.28),
            transparent 32%
        ),

        linear-gradient(
            135deg,
            #7b326f 0%,
            #592254 32%,
            #42163f 68%,
            #2c0d2c 100%
        );
}


/* =========================================================
   GLOWING BACKGROUND
========================================================= */

.app::before {

    content: "";

    position: absolute;

    width: 550px;
    height: 550px;

    left: 50%;
    top: 50%;

    transform: translate(-50%, -50%);

    background:
        radial-gradient(
            circle,
            rgba(255,173,218,0.15),
            transparent 65%
        );

    filter: blur(15px);

    pointer-events: none;
}


/* =========================================================
   TRANSPARENT HEARTS BACKGROUND
========================================================= */

.bg-heart {

    position: absolute;

    color: rgba(255,205,232,0.16);

    font-family: Arial, sans-serif;

    pointer-events: none;

    animation:
        heartFloat
        var(--speed)
        ease-in-out
        infinite alternate;

    z-index: 1;
}

.h1 {
    left: 5%;
    top: 14%;
    font-size: 52px;
    --speed: 5s;
}

.h2 {
    left: 82%;
    top: 18%;
    font-size: 38px;
    --speed: 6s;
}

.h3 {
    left: 14%;
    top: 72%;
    font-size: 32px;
    --speed: 4.5s;
}

.h4 {
    left: 88%;
    top: 72%;
    font-size: 58px;
    --speed: 5.5s;
}

.h5 {
    left: 47%;
    top: 8%;
    font-size: 28px;
    --speed: 4s;
}

.h6 {
    left: 70%;
    top: 84%;
    font-size: 30px;
    --speed: 6s;
}

.h7 {
    left: 28%;
    top: 35%;
    font-size: 25px;
    --speed: 5s;
}


@keyframes heartFloat {

    from {
        transform: translateY(0) rotate(-8deg);
        opacity: 0.10;
    }

    to {
        transform: translateY(-18px) rotate(8deg);
        opacity: 0.25;
    }
}


/* =========================================================
   SPARKLES
========================================================= */

.sparkle {

    position: absolute;

    width: 4px;
    height: 4px;

    border-radius: 50%;

    background: rgba(255,255,255,0.90);

    box-shadow:
        0 0 9px rgba(255,255,255,0.9);

    pointer-events: none;

    z-index: 2;

    animation:
        sparkleMove
        var(--duration)
        ease-in-out
        infinite;

    animation-delay: var(--delay);
}


@keyframes sparkleMove {

    0% {
        transform:
            translate(0,0)
            scale(0.5);

        opacity: 0.15;
    }

    50% {
        transform:
            translate(var(--moveX), var(--moveY))
            scale(1.5);

        opacity: 1;
    }

    100% {
        transform:
            translate(
                calc(var(--moveX) * -0.5),
                calc(var(--moveY) * -0.5)
            )
            scale(0.5);

        opacity: 0.15;
    }
}


/* =========================================================
   PAGE SYSTEM
========================================================= */

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


/* =========================================================
   TEXT
========================================================= */

.small-title {

    font-size: 23px;

    letter-spacing: 1px;

    margin-bottom: 18px;

    color: #ffeaf6;
}


.big-title {

    font-family: "Delius", cursive;

    font-size: 43px;

    line-height: 1.15;

    color: white;

    text-shadow:
        0 3px 15px rgba(0,0,0,0.25);
}


.sub-title {

    font-size: 23px;

    margin-top: 10px;

    color: #ffe2f2;
}


/* =========================================================
   NEXT BUTTON
========================================================= */

.next-btn {

    margin-top: 25px;

    border: none;

    outline: none;

    padding: 10px 28px;

    border-radius: 30px;

    background:
        linear-gradient(
            180deg,
            #f7acd1,
            #dc78ad
        );

    color: white;

    font-family: "Patrick Hand", cursive;

    font-size: 20px;

    cursor: pointer;

    box-shadow:
        0 6px 20px rgba(0,0,0,0.25);

    transition: 0.25s;
}

.next-btn:hover {

    transform: scale(1.06);
}


/* =========================================================
   PAGE 1 - HEART
========================================================= */

.first-heart-area {

    position: relative;

    width: 270px;

    height: 270px;

    margin-top: 5px;
}


.start-heart {

    position: absolute;

    width: 105px;
    height: 105px;

    left: 82px;
    top: 80px;

    background: #f17fab;

    transform: rotate(-45deg);

    border-radius: 12px;

    box-shadow:
        0 0 30px rgba(255,139,191,0.65);

    cursor: pointer;

    z-index: 5;

    transition: 0.2s;
}


.start-heart::before,
.start-heart::after {

    content: "";

    position: absolute;

    width: 105px;
    height: 105px;

    background: #f17fab;

    border-radius: 50%;
}


.start-heart::before {

    top: -52px;
    left: 0;
}


.start-heart::after {

    top: 0;
    left: 52px;
}


.start-heart:hover {

    transform:
        rotate(-45deg)
        scale(1.08);
}


/* =========================================================
   HEART BLAST
========================================================= */

.blast-heart {

    animation:
        heartBlast
        0.65s
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

        opacity: 1;
    }

    100% {

        transform:
            rotate(-45deg)
            scale(0);

        opacity: 0;
    }
}


/* =========================================================
   PINK SCREEN SPREAD
========================================================= */

.pink-flash {

    position: fixed;

    inset: 0;

    background:
        radial-gradient(
            circle at center,
            #ffd0e5 0%,
            #f49ac5 45%,
            #df75ac 100%
        );

    opacity: 0;

    pointer-events: none;

    z-index: 1000;
}


.pink-flash.show {

    animation:
        pinkSpread
        1.15s
        forwards;
}


@keyframes pinkSpread {

    0% {
        opacity: 0;
        transform: scale(0.2);
    }

    35% {
        opacity: 0.96;
        transform: scale(1);
    }

    100% {
        opacity: 0;
        transform: scale(1.5);
    }
}


/* =========================================================
   PAGE 2 - CAKE
========================================================= */

.cake-page {

    justify-content: center;
}


.cake-area {

    position: relative;

    width: 330px;

    height: 380px;

    margin-top: 5px;

    flex-shrink: 0;
}


.plate {

    position: absolute;

    width: 255px;
    height: 19px;

    bottom: 18px;
    left: 37px;

    border-radius: 50%;

    background:
        rgba(255,255,255,0.88);

    box-shadow:
        0 6px 13px rgba(0,0,0,0.22);
}


/* =========================================================
   CAKE LAYERS
========================================================= */

.cake-layer {

    position: absolute;

    left: 50%;

    transform: translateX(-50%);

    border-radius: 10px;

    background:
        linear-gradient(
            180deg,
            #f8b7d4,
            #df7eaf
        );

    box-shadow:
        0 7px 13px rgba(0,0,0,0.22);

    opacity: 0;
}


.layer3 {

    width: 230px;
    height: 65px;

    bottom: 35px;
}


.layer2 {

    width: 195px;
    height: 60px;

    bottom: 91px;
}


.layer1 {

    width: 155px;
    height: 54px;

    bottom: 145px;
}


/* =========================================================
   CREAM
========================================================= */

.cream {

    position: absolute;

    left: 50%;

    transform: translateX(-50%);

    height: 14px;

    border-radius: 50%;

    background: #fffafd;

    opacity: 0;

    z-index: 5;
}


.cream1 {

    width: 145px;
    bottom: 140px;
}


.cream2 {

    width: 184px;
    bottom: 87px;
}


.cream3 {

    width: 220px;
    bottom: 29px;
}


/* =========================================================
   CANDLE
========================================================= */

.candle {

    position: absolute;

    width: 19px;
    height: 70px;

    left: 50%;
    bottom: 198px;

    transform: translateX(-50%);

    background:
        repeating-linear-gradient(
            -45deg,
            #ffffff,
            #ffffff 8px,
            #efa4c6 8px,
            #efa4c6 16px
        );

    border-radius: 5px;

    opacity: 0;

    z-index: 7;
}


/* =========================================================
   FLAME
========================================================= */

.flame {

    position: absolute;

    width: 18px;
    height: 27px;

    left: 50%;
    bottom: 266px;

    transform:
        translateX(-50%)
        rotate(45deg);

    background: #ffe79c;

    border-radius:
        50% 50% 50% 0;

    opacity: 0;

    box-shadow:
        0 0 18px #ffd67b;

    z-index: 8;
}


/* =========================================================
   CAKE BUILD ANIMATION
========================================================= */

.cake-area.build .layer3 {

    animation:
        layerDrop
        0.65s
        0.15s
        forwards;
}


.cake-area.build .layer2 {

    animation:
        layerDrop
        0.65s
        0.85s
        forwards;
}


.cake-area.build .layer1 {

    animation:
        layerDrop
        0.65s
        1.55s
        forwards;
}


.cake-area.build .cream1 {

    animation:
        creamAppear
        0.45s
        2.10s
        forwards;
}


.cake-area.build .cream2 {

    animation:
        creamAppear
        0.45s
        2.40s
        forwards;
}


.cake-area.build .cream3 {

    animation:
        creamAppear
        0.45s
        2.70s
        forwards;
}


.cake-area.build .candle {

    animation:
        candleDrop
        0.65s
        3.05s
        forwards;
}


.cake-area.build .flame {

    animation:
        flameDrop
        0.55s
        3.45s
        forwards,

        flicker
        0.8s
        4s
        infinite
        alternate;
}


/* =========================================================
   LAYER DROP
========================================================= */

@keyframes layerDrop {

    0% {

        transform:
            translate(-50%, -280px)
            scale(0.9);

        opacity: 0;
    }

    70% {

        transform:
            translate(-50%, 8px)
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
            scaleX(0.35);
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
            translate(-50%, -170px)
            rotate(-10deg);
    }

    75% {

        transform:
            translate(-50%, 7px)
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


/* =========================================================
   HAPPY BIRTHDAY UNDER CAKE
========================================================= */

.cake-message {

    width: 100%;

    margin-top: 8px;

    font-family:
        "Delius",
        cursive;

    font-size: 34px;

    line-height: 1.15;

    color: white;

    opacity: 0;

    text-shadow:
        0 3px 12px rgba(0,0,0,0.25);
}


.cake-message.show {

    animation:
        cakeTextAppear
        0.9s
        4s
        forwards;
}


@keyframes cakeTextAppear {

    from {

        opacity: 0;

        transform:
            translateY(18px)
            scale(0.9);
    }

    to {

        opacity: 1;

        transform:
            translateY(0)
            scale(1);
    }
}


/* =========================================================
   PAGE 3 - BALLOONS
========================================================= */

.balloon-page {

    justify-content: center;
}


.balloon-title {

    font-size: 27px;

    margin-bottom: 22px;

    color: #ffeaf5;
}


.balloon-area {

    width: 360px;

    height: 390px;

    position: relative;
}


/* =========================================================
   BALLOONS
========================================================= */

.balloon {

    position: absolute;

    width: 75px;
    height: 96px;

    border-radius:
        50% 50% 45% 45%;

    cursor: pointer;

    transition: 0.15s;

    box-shadow:

        inset -12px -9px 18px
        rgba(0,0,0,0.13),

        inset 8px 5px 10px
        rgba(255,255,255,0.28);

    z-index: 4;
}


.balloon::after {

    content: "";

    position: absolute;

    width: 2px;

    height: 92px;

    background:
        rgba(255,255,255,0.60);

    top: 94px;

    left: 50%;
}


.balloon::before {

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

    left: 38px;
    top: 50px;

    background: #f5a5c8;
    color: #f5a5c8;
}


.b2 {

    left: 137px;
    top: 8px;

    background: #dfabd8;
    color: #dfabd8;
}


.b3 {

    left: 230px;
    top: 52px;

    background: #a9c2dc;
    color: #a9c2dc;
}


.b4 {

    left: 135px;
    top: 135px;

    background: #f1bdd9;
    color: #f1bdd9;
}


.balloon:hover {

    transform:
        translateY(-5px)
        scale(1.05);
}


.balloon.popped {

    animation:
        popBalloon
        0.38s
        forwards;
}


@keyframes popBalloon {

    0% {

        transform: scale(1);

        opacity: 1;
    }

    45% {

        transform: scale(1.35);

        opacity: 0.85;
    }

    100% {

        transform: scale(0);

        opacity: 0;
    }
}


/* =========================================================
   BALLOON MESSAGE
========================================================= */

.balloon-message {

    position: absolute;

    width: 325px;

    left: 50%;

    bottom: 10px;

    transform:
        translateX(-50%)
        translateY(20px);

    padding: 14px 19px;

    border-radius: 18px;

    background:
        rgba(245,158,198,0.28);

    border:
        1px solid
        rgba(255,225,240,0.40);

    box-shadow:
        0 7px 22px
        rgba(0,0,0,0.13);

    backdrop-filter:
        blur(4px);

    -webkit-backdrop-filter:
        blur(4px);

    font-size: 21px;

    line-height: 1.2;

    color: #fff8fc;

    opacity: 0;

    transition:
        opacity 0.45s ease,
        transform 0.45s ease;
}


.balloon-message.show {

    opacity: 1;

    transform:
        translateX(-50%)
        translateY(0);
}


/* =========================================================
   PAGE 4 - PHOTOS
========================================================= */

.memory-title {

    font-size: 27px;

    margin-bottom: 25px;

    color: #ffeaf5;
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
        0 10px 25px
        rgba(0,0,0,0.25);

    transform:
        rotate(-2deg);

    transition: 0.3s;
}


.photo-card:nth-child(2) {

    transform:
        rotate(2deg);
}


.photo-card:nth-child(3) {

    transform:
        rotate(-1deg);
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


/* =========================================================
   PAGE 5 - ENVELOPE
========================================================= */

.envelope-page {

    justify-content: center;
}


.envelope-wrapper {

    width: 330px;

    height: 230px;

    position: relative;

    cursor: pointer;

    animation:
        envelopeEnter
        1.2s
        ease-out
        forwards;
}


@keyframes envelopeEnter {

    0% {

        transform:
            translateX(-120vw)
            rotate(-8deg);

        opacity: 0;
    }

    65% {

        transform:
            translateX(25px)
            rotate(2deg);

        opacity: 1;
    }

    100% {

        transform:
            translateX(0)
            rotate(0);

        opacity: 1;
    }
}


.envelope {

    position: absolute;

    width: 300px;
    height: 190px;

    left: 15px;
    top: 20px;

    background: #f5d5c6;

    border-radius: 8px;

    box-shadow:
        0 12px 28px
        rgba(0,0,0,0.30);

    overflow: hidden;
}


.envelope::before {

    content: "";

    position: absolute;

    left: 0;
    top: 0;

    width: 0;
    height: 0;

    border-left:
        150px solid transparent;

    border-right:
        150px solid transparent;

    border-top:
        105px solid #e8bcae;

    z-index: 3;

    transform-origin: top center;

    transition:
        transform 0.8s ease;
}


.envelope::after {

    content: "";

    position: absolute;

    left: 0;
    bottom: 0;

    width: 0;
    height: 0;

    border-left:
        150px solid #dca99e;

    border-top:
        95px solid transparent;

    border-bottom:
        95px solid transparent;

    z-index: 4;
}


.envelope-right {

    position: absolute;

    right: 0;
    bottom: 0;

    width: 0;
    height: 0;

    border-right:
        150px solid #d6a097;

    border-top:
        95px solid transparent;

    border-bottom:
        95px solid transparent;

    z-index: 4;
}


.envelope-letter-preview {

    position: absolute;

    width: 190px;
    height: 105px;

    left: 55px;
    top: 38px;

    background: #fff8ec;

    z-index: 2;

    border-radius: 3px;

    color: #65334e;

    padding: 18px 10px;

    font-family:
        "Delius",
        cursive;

    font-size: 17px;

    box-shadow:
        0 2px 8px
        rgba(0,0,0,0.15);
}


.envelope-page::after {

    content:
        "Tap the letter";

    margin-top: 18px;

    font-size: 21px;

    color: #ffe8f4;

    animation:
        hintPulse
        1.5s
        infinite;
}


@keyframes hintPulse {

    0%, 100% {
        opacity: 0.55;
    }

    50% {
        opacity: 1;
    }
}


/* =========================================================
   FULL LETTER
========================================================= */

.letter-full {

    position: fixed;

    inset: 0;

    display: none;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    padding: 35px;

    background:

        radial-gradient(
            circle at 50% 30%,
            rgba(255,201,225,0.25),
            transparent 40%
        ),

        linear-gradient(
            135deg,
            #7b326f,
            #4c1c49,
            #321032
        );

    z-index: 2000;

    opacity: 0;
}


.letter-full.open {

    display: flex;

    animation:
        letterOpen
        0.9s
        forwards;
}


@keyframes letterOpen {

    from {

        opacity: 0;

        transform:
            scale(0.92);
    }

    to {

        opacity: 1;

        transform:
            scale(1);
    }
}


.letter-paper {

    width: min(700px, 92vw);

    min-height: 430px;

    padding: 55px 45px;

    background:
        linear-gradient(
            180deg,
            #fffaf1,
            #fff3e2
        );

    color: #5b2948;

    border-radius: 5px;

    box-shadow:
        0 18px 45px
        rgba(0,0,0,0.35);

    position: relative;

    font-family:
        "Patrick Hand",
        cursive;
}


.letter-paper h1 {

    font-family:
        "Delius",
        cursive;

    font-size: 42px;

    line-height: 1.15;

    margin:
        0 0 25px;

    color: #742e5d;
}


.letter-paper p {

    font-size: 24px;

    line-height: 1.45;

    margin:
        12px 0;
}


.letter-from {

    margin-top: 30px;

    font-size: 25px;

    text-align: right;

    color: #742e5d;
}


.close-letter {

    margin-top: 18px;

    border: none;

    padding: 9px 22px;

    border-radius: 25px;

    background: rgba(255,190,220,0.75);

    color: #652847;

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 19px;

    cursor: pointer;
}


/* =========================================================
   FINAL PAGE
========================================================= */

.final-page {

    justify-content: center;

    overflow: hidden;
}


.final-heart {

    position: relative;

    width: 145px;

    height: 145px;

    margin-bottom: 20px;

    animation:
        finalHeartPop
        0.9s
        cubic-bezier(.17,.67,.36,1.4)
        both;
}


.final-heart-shape {

    position: absolute;

    width: 110px;
    height: 110px;

    left: 18px;
    top: 20px;

    background: #f28ab4;

    transform: rotate(-45deg);

    border-radius: 14px;

    box-shadow:
        0 0 40px
        rgba(255,142,192,0.60);
}


.final-heart-shape::before,
.final-heart-shape::after {

    content: "";

    position: absolute;

    width: 110px;
    height: 110px;

    background: #f28ab4;

    border-radius: 50%;
}


.final-heart-shape::before {

    top: -55px;
    left: 0;
}


.final-heart-shape::after {

    top: 0;
    left: 55px;
}


@keyframes finalHeartPop {

    0% {

        transform:
            scale(0);

        opacity: 0;
    }

    65% {

        transform:
            scale(1.18);

        opacity: 1;
    }

    100% {

        transform:
            scale(1);

        opacity: 1;
    }
}


.final-title {

    font-family:
        "Delius",
        cursive;

    font-size: 47px;

    line-height: 1.15;

    color: white;

    text-shadow:
        0 4px 16px rgba(0,0,0,0.25);

    animation:
        finalTextPop
        0.9s
        0.45s
        both;
}


@keyframes finalTextPop {

    from {

        opacity: 0;

        transform:
            translateY(25px)
            scale(0.9);
    }

    to {

        opacity: 1;

        transform:
            translateY(0)
            scale(1);
    }
}


/* =========================================================
   COLOUR PAPER PIECES
========================================================= */

.paper-piece {

    position: fixed;

    width: 10px;
    height: 17px;

    top: 50%;

    left: 50%;

    z-index: 6000;

    pointer-events: none;

    opacity: 0;

    animation:
        paperPop
        1.8s
        ease-out
        forwards;
}


@keyframes paperPop {

    0% {

        opacity: 0;

        transform:
            translate(-50%, -50%)
            rotate(0deg)
            scale(0.4);
    }

    15% {

        opacity: 1;
    }

    100% {

        opacity: 1;

        transform:
            translate(
                var(--x),
                var(--y)
            )
            rotate(var(--rotate))
            scale(1);
    }
}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 700px) {

    .big-title {
        font-size: 35px;
    }

    .sub-title {
        font-size: 20px;
    }

    .photo-container {
        gap: 8px;
        transform: scale(0.88);
    }

    .photo-card {
        width: 30vw;
        max-width: 190px;
    }

    .photo-card img {
        height: 190px;
    }

    .letter-paper {
        min-height: 390px;
        padding: 38px 25px;
    }

    .letter-paper h1 {
        font-size: 32px;
    }

    .letter-paper p {
        font-size: 21px;
    }

    .final-title {
        font-size: 37px;
    }
}

</style>

</head>


<body>


<div class="app" id="app">


<!-- =====================================================
     BACKGROUND HEARTS
===================================================== -->

<div class="bg-heart h1">♥</div>
<div class="bg-heart h2">♥</div>
<div class="bg-heart h3">♥</div>
<div class="bg-heart h4">♥</div>
<div class="bg-heart h5">♥</div>
<div class="bg-heart h6">♥</div>
<div class="bg-heart h7">♥</div>


<!-- =====================================================
     SPARKLES
===================================================== -->

<div class="sparkle"
     style="left:12%;top:20%;--moveX:20px;--moveY:-30px;--duration:4s;--delay:0s;"></div>

<div class="sparkle"
     style="left:25%;top:65%;--moveX:-25px;--moveY:-20px;--duration:5s;--delay:1s;"></div>

<div class="sparkle"
     style="left:75%;top:25%;--moveX:25px;--moveY:25px;--duration:4.5s;--delay:0.5s;"></div>

<div class="sparkle"
     style="left:88%;top:58%;--moveX:-20px;--moveY:30px;--duration:5.5s;--delay:1.5s;"></div>

<div class="sparkle"
     style="left:50%;top:75%;--moveX:30px;--moveY:-25px;--duration:4s;--delay:2s;"></div>


<!-- =====================================================
     PINK FLASH
===================================================== -->

<div class="pink-flash" id="pinkFlash"></div>


<!-- =====================================================
     PAGE 1
===================================================== -->

<section class="page active" id="page1">

    <div class="small-title">
        A little surprise for you
    </div>

    <div class="big-title">
        Something special<br>
        is waiting...
    </div>

    <div class="sub-title">
        Touch the heart
    </div>

    <div class="first-heart-area">

        <div
            class="start-heart"
            id="startHeart"
            onclick="startSurprise()">
        </div>

    </div>

</section>


<!-- =====================================================
     PAGE 2 - CAKE
===================================================== -->

<section class="page cake-page" id="page2">

    <div class="small-title">
        And here comes your birthday cake...
    </div>

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

    </div>

    <!-- HAPPY BIRTHDAY IS BELOW THE CAKE -->

    <div class="cake-message" id="cakeMessage">
        Happy Birthday Ricky
    </div>

    <button
        class="next-btn"
        id="cakeNext"
        style="display:none;"
        onclick="showPage(3)">
        Continue
    </button>

</section>


<!-- =====================================================
     PAGE 3 - BALLOONS
===================================================== -->

<section class="page balloon-page" id="page3">

    <div class="balloon-title">
        Pop the balloons
    </div>

    <div class="balloon-area">

        <div
            class="balloon b1"
            onclick="popBalloon(this, 1)">
        </div>

        <div
            class="balloon b2"
            onclick="popBalloon(this, 2)">
        </div>

        <div
            class="balloon b3"
            onclick="popBalloon(this, 3)">
        </div>

        <div
            class="balloon b4"
            onclick="popBalloon(this, 4)">
        </div>


        <div
            class="balloon-message"
            id="balloonMessage">
        </div>

    </div>

    <button
        class="next-btn"
        id="balloonNext"
        style="display:none;"
        onclick="showPage(4)">
        Continue
    </button>

</section>


<!-- =====================================================
     PAGE 4 - PHOTOS
===================================================== -->

<section class="page" id="page4">

    <div class="memory-title">
        A little collection of you
    </div>

    <div class="photo-container">


        <div class="photo-card">

            <img
                src="data:image/jpeg;base64,__PHOTO1__"
                alt="Photo 1">

            <div class="photo-caption">
                One of my favourite pictures of you
            </div>

        </div>


        <div class="photo-card">

            <img
                src="data:image/jpeg;base64,__PHOTO2__"
                alt="Photo 2">

            <div class="photo-caption">
                A moment I really love
            </div>

        </div>


        <div class="photo-card">

            <img
                src="data:image/jpeg;base64,__PHOTO3__"
                alt="Photo 3">

            <div class="photo-caption">
                A picture that always makes me smile
            </div>

        </div>


    </div>


    <button
        class="next-btn"
        onclick="showPage(5)">
        Continue
    </button>

</section>


<!-- =====================================================
     PAGE 5 - ENVELOPE
===================================================== -->

<section class="page envelope-page" id="page5">

    <div class="small-title">
        There is one more thing...
    </div>

    <div
        class="envelope-wrapper"
        onclick="openLetter()">

        <div class="envelope">

            <div class="envelope-letter-preview">
                For you...
            </div>

            <div class="envelope-right"></div>

        </div>

    </div>

</section>


<!-- =====================================================
     FULL LETTER
===================================================== -->

<div
    class="letter-full"
    id="letterFull">

    <div class="letter-paper">

        <h1>
            Happy Birthday my dear Rickyluu❤️
        </h1>

        <p>
            Today is your special day, so I just wanted
            to make a little something for you.
        </p>

        <p>
            I hope this birthday brings you lots of
            happiness, beautiful moments and reasons
            to smile.
        </p>

        <p>
            Keep smiling and keep being the wonderful
            person you are.
        </p>

        <div class="letter-from">
            From your Maggi
        </div>

    </div>

    <button
        class="close-letter"
        onclick="closeLetter()">
        Continue
    </button>

</div>


<!-- =====================================================
     PAGE 6 - FINAL
===================================================== -->

<section class="page final-page" id="page6">

    <div class="final-heart">

        <div class="final-heart-shape"></div>

    </div>

    <div class="final-title">
        Happy Birthday Ricky 😽🌷💗
    </div>

</section>


</div>


<script>

/* =========================================================
   PAGE CONTROL
========================================================= */

let currentPage = 1;


function showPage(number) {

    document
        .querySelectorAll(".page")
        .forEach(function(page) {

            page.classList.remove("active");

        });


    const nextPage =
        document.getElementById("page" + number);


    if (nextPage) {

        nextPage.classList.add("active");

        currentPage = number;

    }


    if (number === 2) {

        startCake();

    }


    if (number === 6) {

        createPaperPieces();

    }
}


/* =========================================================
   PAGE 1 - HEART
========================================================= */

function startSurprise() {

    const heart =
        document.getElementById("startHeart");

    const flash =
        document.getElementById("pinkFlash");


    heart.classList.add("blast-heart");

    createHeartParticles();

    setTimeout(function() {

        flash.classList.add("show");

    }, 180);


    setTimeout(function() {

        showPage(2);

    }, 720);


    setTimeout(function() {

        flash.classList.remove("show");

    }, 1500);
}


/* =========================================================
   HEART PARTICLES
========================================================= */

function createHeartParticles() {

    const colors = [
        "#f7a5c9",
        "#ffd0e4",
        "#e984b5",
        "#ffffff"
    ];


    for (let i = 0; i < 26; i++) {

        const piece =
            document.createElement("div");


        piece.className = "particle";


        const angle =
            Math.random() * Math.PI * 2;


        const distance =
            80 + Math.random() * 180;


        piece.style.left = "50%";
        piece.style.top = "50%";


        piece.style.background =
            colors[
                Math.floor(
                    Math.random() * colors.length
                )
            ];


        piece.style.borderRadius =
            Math.random() > 0.5
                ? "50%"
                : "2px";


        piece.style.setProperty(
            "--x",
            Math.cos(angle) * distance + "px"
        );


        piece.style.setProperty(
            "--y",
            Math.sin(angle) * distance + "px"
        );


        document.body.appendChild(piece);


        setTimeout(function() {

            piece.remove();

        }, 1300);
    }
}


/* =========================================================
   CAKE
========================================================= */

function startCake() {

    const cake =
        document.getElementById("cakeArea");

    const message =
        document.getElementById("cakeMessage");

    const next =
        document.getElementById("cakeNext");


    cake.classList.remove("build");

    message.classList.remove("show");

    next.style.display = "none";


    void cake.offsetWidth;


    cake.classList.add("build");


    message.classList.add("show");


    setTimeout(function() {

        next.style.display = "inline-block";

    }, 5200);
}


/* =========================================================
   BALLOONS
========================================================= */

const balloonMessages = {

    1:
        "You deserve all the happiness in the world.",

    2:
        "May this birthday bring you many beautiful memories.",

    3:
        "Keep smiling because your smile makes everything brighter.",

    4:
        "Wishing you a year full of happiness and wonderful moments."
};


let poppedCount = 0;


function popBalloon(balloon, number) {

    if (balloon.classList.contains("popped")) {

        return;

    }


    balloon.classList.add("popped");


    poppedCount++;


    const message =
        document.getElementById("balloonMessage");


    message.innerText =
        balloonMessages[number];


    message.classList.remove("show");


    setTimeout(function() {

        message.classList.add("show");

    }, 80);


    createBalloonPieces(balloon);


    if (poppedCount >= 4) {

        setTimeout(function() {

            document
                .getElementById("balloonNext")
                .style.display = "inline-block";

        }, 500);
    }
}


/* =========================================================
   BALLOON POP PARTICLES
========================================================= */

function createBalloonPieces(balloon) {

    const rect =
        balloon.getBoundingClientRect();


    const colors = [
        "#f5a5c8",
        "#e4b2dc",
        "#b4cbe2",
        "#f6c1da"
    ];


    for (let i = 0; i < 10; i++) {

        const piece =
            document.createElement("div");


        piece.className = "particle";


        piece.style.left =
            rect.left + rect.width / 2 + "px";


        piece.style.top =
            rect.top + rect.height / 2 + "px";


        const angle =
            Math.random() * Math.PI * 2;


        const distance =
            30 + Math.random() * 70;


        piece.style.background =
            colors[
                Math.floor(
                    Math.random() * colors.length
                )
            ];


        piece.style.setProperty(
            "--x",
            Math.cos(angle) * distance + "px"
        );


        piece.style.setProperty(
            "--y",
            Math.sin(angle) * distance + "px"
        );


        document.body.appendChild(piece);


        setTimeout(function() {

            piece.remove();

        }, 1300);
    }
}


/* =========================================================
   ENVELOPE
========================================================= */

function openLetter() {

    const letter =
        document.getElementById("letterFull");


    letter.classList.add("open");
}


function closeLetter() {

    const letter =
        document.getElementById("letterFull");


    letter.classList.remove("open");


    setTimeout(function() {

        showPage(6);

    }, 300);
}


/* =========================================================
   FINAL COLOUR PAPER PIECES
========================================================= */

function createPaperPieces() {

    const colors = [
        "#f5a3c7",
        "#f6d18d",
        "#a8c7df",
        "#d9a7d2",
        "#ffffff",
        "#e99ab9",
        "#c5dcae"
    ];


    for (let i = 0; i < 45; i++) {

        const piece =
            document.createElement("div");


        piece.className = "paper-piece";


        const side =
            Math.random() > 0.5
                ? 1
                : -1;


        const x =
            side *
            (120 + Math.random() * 500);


        const y =
            -80 +
            Math.random() * 700;


        const rotate =
            Math.random() * 720 - 360;


        piece.style.background =
            colors[
                Math.floor(
                    Math.random() * colors.length
                )
            ];


        piece.style.setProperty(
            "--x",
            x + "px"
        );


        piece.style.setProperty(
            "--y",
            y + "px"
        );


        piece.style.setProperty(
            "--rotate",
            rotate + "deg"
        );


        piece.style.left =
            "50%";


        piece.style.top =
            "50%";


        document.body.appendChild(piece);


        setTimeout(function() {

            piece.remove();

        }, 2200);
    }
}

</script>

</body>

</html>
"""


# =========================================================
# INSERT PHOTOS
# =========================================================

html = html.replace(
    "__PHOTO1__",
    photo1
)

html = html.replace(
    "__PHOTO2__",
    photo2
)

html = html.replace(
    "__PHOTO3__",
    photo3
)


# =========================================================
# RUN APP
# =========================================================

components.html(
    html,
    height=850,
    scrolling=False
)
