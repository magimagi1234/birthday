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
}


/* =========================================================
   MAIN BACKGROUND
   BRIGHT PURPLE / PINK GLOW LIKE VIDEO
========================================================= */

.app {

    position: relative;

    width: 100%;
    height: 100vh;
    min-height: 700px;

    overflow: hidden;

    color: white;

    background:

        radial-gradient(
            circle at 50% 25%,
            rgba(221, 119, 205, 0.62),
            transparent 28%
        ),

        radial-gradient(
            circle at 15% 65%,
            rgba(184, 72, 173, 0.45),
            transparent 30%
        ),

        radial-gradient(
            circle at 85% 70%,
            rgba(208, 87, 181, 0.42),
            transparent 30%
        ),

        linear-gradient(
            180deg,
            #70266f 0%,
            #581756 38%,
            #3b103b 72%,
            #230823 100%
        );
}


/* =========================================================
   EXTRA GLOW
========================================================= */

.app::before {

    content: "";

    position: absolute;

    width: 650px;
    height: 650px;

    left: 50%;
    top: 35%;

    transform: translate(-50%, -50%);

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(255, 150, 220, 0.18),
            transparent 65%
        );

    filter: blur(20px);

    pointer-events: none;
}


/* =========================================================
   MOVING SPARKLES
========================================================= */

.sparkle {

    position: absolute;

    width: 4px;
    height: 4px;

    border-radius: 50%;

    background: white;

    box-shadow:
        0 0 7px white,
        0 0 15px rgba(255, 200, 240, 0.9);

    pointer-events: none;

    opacity: 0.3;

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
            translate(0, 0)
            scale(0.4);

        opacity: 0.15;
    }

    25% {
        opacity: 0.8;
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
        opacity: 0.55;
    }

    100% {

        transform:
            translate(
                calc(var(--moveX) * -0.7),
                calc(var(--moveY) * -0.6)
            )
            scale(0.4);

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

    font-size: 21px;

    color: #fff5fb;

    margin-bottom: 18px;

    letter-spacing: 1px;
}


.big-title {

    font-family: "Delius", cursive;

    font-size: 42px;

    line-height: 1.15;

    color: white;

    text-shadow:
        0 3px 12px rgba(0,0,0,0.25);
}


.sub-title {

    font-size: 22px;

    margin-top: 8px;

    color: #ffe6f3;
}


/* =========================================================
   NEXT BUTTON
========================================================= */

.next-btn {

    border: none;
    outline: none;

    margin-top: 22px;

    padding: 9px 28px;

    border-radius: 30px;

    background:
        linear-gradient(
            180deg,
            #f5b1d1,
            #df82b2
        );

    color: white;

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 20px;

    cursor: pointer;

    box-shadow:
        0 6px 20px rgba(0,0,0,0.25);

    transition: 0.25s;
}

.next-btn:hover {

    transform:
        scale(1.07);
}


/* =========================================================
   PAGE 1 - HEART
========================================================= */

.first-heart-page {

    justify-content: center;
}


/* heart area */

.first-heart-area {

    position: relative;

    width: 300px;
    height: 300px;

    margin-top: 5px;
}


/* heart */

.start-heart {

    position: absolute;

    width: 105px;
    height: 105px;

    left: 98px;
    top: 92px;

    background: #f18bb6;

    transform:
        rotate(-45deg);

    border-radius: 13px;

    box-shadow:
        0 0 30px rgba(255, 155, 205, 0.6),
        0 0 65px rgba(255, 120, 190, 0.25);

    z-index: 5;

    transition: 0.2s;
}


.start-heart::before,
.start-heart::after {

    content: "";

    position: absolute;

    width: 105px;
    height: 105px;

    background: #f18bb6;

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


/* =========================================================
   ARROW - STARTS AT CORNER
========================================================= */

.arrow {

    position: absolute;

    left: -10px;
    bottom: 10px;

    width: 115px;
    height: 7px;

    background: #6c2946;

    border-radius: 10px;

    transform:
        rotate(-28deg);

    transform-origin: left center;

    cursor: pointer;

    z-index: 20;

    box-shadow:
        0 2px 5px rgba(0,0,0,0.2);

    transition:
        left 0.7s ease,
        bottom 0.7s ease,
        transform 0.7s ease;
}


.arrow::after {

    content: "";

    position: absolute;

    right: -3px;
    top: -7px;

    border-left:
        20px solid #6c2946;

    border-top:
        10px solid transparent;

    border-bottom:
        10px solid transparent;
}


/* arrow travels to heart */

.arrow.shoot {

    left: 120px;
    bottom: 143px;

    transform:
        rotate(-45deg);
}


/* =========================================================
   HEART BLAST
========================================================= */

.start-heart.blast {

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

        opacity: 0.85;
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
            circle,
            #ffd0e5,
            #f39ac5 45%,
            #b95491 100%
        );

    opacity: 0;

    pointer-events: none;

    z-index: 9000;
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
    }

    20% {
        opacity: 0.98;
    }

    65% {
        opacity: 0.75;
    }

    100% {
        opacity: 0;
    }
}


/* =========================================================
   PARTICLES
========================================================= */

.particle {

    position: fixed;

    width: 8px;
    height: 8px;

    border-radius: 50%;

    background: #ffd9eb;

    pointer-events: none;

    z-index: 9500;

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


/* =========================================================
   PAGE 2 - CAKE
========================================================= */

.cake-page {

    justify-content: center;
}


.cake-area {

    position: relative;

    width: 330px;
    height: 410px;

    margin-top: 0;
}


/* plate */

.plate {

    position: absolute;

    width: 255px;
    height: 20px;

    left: 37px;
    bottom: 42px;

    border-radius: 50%;

    background: rgba(255,255,255,0.85);

    box-shadow:
        0 5px 12px rgba(0,0,0,0.25);
}


/* cake layers */

.cake-layer {

    position: absolute;

    left: 50%;

    transform:
        translateX(-50%);

    border-radius: 10px;

    background:
        linear-gradient(
            180deg,
            #f8b5d3,
            #dc7cab
        );

    box-shadow:
        0 7px 13px rgba(0,0,0,0.22);

    opacity: 0;
}


.layer3 {

    width: 230px;
    height: 67px;

    bottom: 59px;
}


.layer2 {

    width: 195px;
    height: 62px;

    bottom: 117px;
}


.layer1 {

    width: 155px;
    height: 55px;

    bottom: 170px;
}


/* cream */

.cream {

    position: absolute;

    left: 50%;

    transform:
        translateX(-50%);

    height: 14px;

    border-radius: 50%;

    background: #fffaff;

    opacity: 0;

    z-index: 5;
}


.cream1 {

    width: 145px;
    bottom: 165px;
}


.cream2 {

    width: 184px;
    bottom: 112px;
}


.cream3 {

    width: 220px;
    bottom: 55px;
}


/* candle */

.candle {

    position: absolute;

    width: 19px;
    height: 75px;

    left: 50%;
    bottom: 225px;

    transform:
        translateX(-50%);

    background:
        repeating-linear-gradient(
            -45deg,
            #ffffff 0px,
            #ffffff 8px,
            #f0a2c6 8px,
            #f0a2c6 16px
        );

    border-radius: 5px;

    opacity: 0;

    z-index: 7;
}


/* flame */

.flame {

    position: absolute;

    width: 18px;
    height: 27px;

    left: 50%;
    bottom: 295px;

    transform:
        translateX(-50%)
        rotate(45deg);

    background: #ffe89b;

    border-radius:
        50% 50% 50% 0;

    opacity: 0;

    z-index: 8;

    box-shadow:
        0 0 18px #ffd878;
}


/* cake animation */

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


/* HAPPY BIRTHDAY BELOW CAKE */

.cake-message {

    position: absolute;

    left: 50%;

    bottom: -3px;

    transform:
        translateX(-50%);

    width: 100%;

    font-family:
        "Delius",
        cursive;

    font-size: 35px;

    line-height: 1.1;

    color: white;

    opacity: 0;
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
            translateX(-50%)
            translateY(18px);
    }

    to {

        opacity: 1;

        transform:
            translateX(-50%)
            translateY(0);
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

    margin-bottom: 15px;

    color: #fff8fc;
}


.balloon-area {

    position: relative;

    width: 370px;
    height: 390px;
}


/* balloons */

.balloon {

    position: absolute;

    width: 76px;
    height: 98px;

    border-radius:
        50% 50% 46% 46%;

    cursor: pointer;

    z-index: 5;

    box-shadow:

        inset -12px -10px 18px
        rgba(0,0,0,0.12),

        inset 8px 6px 12px
        rgba(255,255,255,0.35);

    transition:
        transform 0.2s;
}


.balloon::after {

    content: "";

    position: absolute;

    width: 2px;
    height: 110px;

    top: 94px;
    left: 50%;

    background:
        rgba(255,255,255,0.65);
}


.balloon::before {

    content: "";

    position: absolute;

    width: 0;
    height: 0;

    bottom: -7px;
    left: 50%;

    transform:
        translateX(-50%);

    border-left:
        6px solid transparent;

    border-right:
        6px solid transparent;

    border-top:
        10px solid currentColor;
}


.b1 {

    left: 35px;
    top: 50px;

    background: #f3a8c9;
    color: #f3a8c9;
}


.b2 {

    left: 145px;
    top: 5px;

    background: #e6afd9;
    color: #e6afd9;
}


.b3 {

    left: 255px;
    top: 52px;

    background: #a9cfe0;
    color: #a9cfe0;
}


.b4 {

    left: 145px;
    top: 145px;

    background: #f2b8d5;
    color: #f2b8d5;
}


.balloon:hover {

    transform:
        translateY(-6px)
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

        transform:
            scale(1);

        opacity: 1;
    }

    45% {

        transform:
            scale(1.35);

        opacity: 0.8;
    }

    100% {

        transform:
            scale(0);

        opacity: 0;
    }
}


/* =========================================================
   BALLOON MESSAGE - TRANSPARENT PINK BOX
========================================================= */

.balloon-message {

    position: absolute;

    left: 50%;
    bottom: 0;

    width: 330px;

    transform:
        translateX(-50%)
        translateY(20px);

    padding: 14px 20px;

    border-radius: 18px;

    background:
        rgba(246, 157, 199, 0.32);

    border:
        1px solid
        rgba(255, 225, 240, 0.42);

    box-shadow:
        0 7px 22px rgba(0,0,0,0.13);

    backdrop-filter:
        blur(4px);

    -webkit-backdrop-filter:
        blur(4px);

    color: #fff9fc;

    font-size: 21px;

    line-height: 1.2;

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


/* =========================================================
   PAGE 4 - PHOTOS
========================================================= */

.memory-title {

    font-size: 27px;

    margin-bottom: 22px;

    color: #fff8fc;
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
        rgba(0,0,0,0.28);

    transform:
        rotate(-2deg);

    transition:
        0.3s;
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


.envelope-area {

    position: relative;

    width: 340px;
    height: 300px;

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
            translateX(-600px);

        opacity: 0;
    }

    70% {

        transform:
            translateX(35px);

        opacity: 1;
    }

    100% {

        transform:
            translateX(0);

        opacity: 1;
    }
}


/* envelope */

.envelope {

    position: absolute;

    width: 280px;
    height: 185px;

    left: 30px;
    top: 55px;

    background:
        linear-gradient(
            135deg,
            #f6bfd8,
            #e98db8
        );

    border-radius: 8px;

    box-shadow:
        0 15px 35px
        rgba(0,0,0,0.28);

    z-index: 5;
}


/* envelope lower folds */

.envelope::before {

    content: "";

    position: absolute;

    left: 0;
    bottom: 0;

    width: 0;
    height: 0;

    border-left:
        140px solid transparent;

    border-right:
        140px solid transparent;

    border-bottom:
        100px solid #dc79aa;

    z-index: 2;
}


/* side folds */

.envelope::after {

    content: "";

    position: absolute;

    left: 0;
    top: 0;

    width: 0;
    height: 0;

    border-left:
        140px solid #f1a6c9;

    border-top:
        92px solid transparent;

    border-bottom:
        92px solid transparent;

    opacity: 0.9;

    z-index: 3;
}


/* flap */

.envelope-flap {

    position: absolute;

    left: 0;
    top: 0;

    width: 0;
    height: 0;

    border-left:
        140px solid transparent;

    border-right:
        140px solid transparent;

    border-top:
        105px solid #f7c6dd;

    transform-origin: top center;

    transition:
        0.8s ease;

    z-index: 8;
}


/* heart seal */

.seal {

    position: absolute;

    left: 50%;
    top: 88px;

    width: 30px;
    height: 30px;

    transform:
        translateX(-50%)
        rotate(-45deg);

    background: #e477a9;

    border-radius: 6px;

    z-index: 10;

    transition:
        0.5s;
}


.seal::before,
.seal::after {

    content: "";

    position: absolute;

    width: 30px;
    height: 30px;

    background: #e477a9;

    border-radius: 50%;
}


.seal::before {

    top: -15px;
    left: 0;
}


.seal::after {

    top: 0;
    left: 15px;
}


/* click hint */

.envelope-hint {

    position: absolute;

    width: 100%;

    bottom: 5px;

    left: 0;

    font-size: 21px;

    color: #ffeaf5;

    z-index: 20;
}


/* =========================================================
   FULL LETTER
========================================================= */

.letter {

    position: absolute;

    left: 50%;
    top: 50%;

    width: min(620px, 88vw);
    min-height: 560px;

    transform:
        translate(-50%, -50%)
        scale(0.15);

    opacity: 0;

    pointer-events: none;

    padding: 42px 38px;

    background:
        linear-gradient(
            135deg,
            #fffdf8,
            #fff7fa
        );

    border-radius: 5px;

    box-shadow:
        0 20px 55px
        rgba(0,0,0,0.35);

    color: #54213f;

    text-align: left;

    z-index: 100;

    transition:
        transform 0.9s cubic-bezier(.17,.89,.32,1.25),
        opacity 0.55s;
}


.envelope-area.open .letter {

    transform:
        translate(-50%, -50%)
        scale(1);

    opacity: 1;

    pointer-events: auto;
}


.envelope-area.open .envelope {

    opacity: 0;

    transform:
        scale(0.5);

    transition:
        0.5s;
}


.envelope-area.open .envelope-flap,
.envelope-area.open .seal,
.envelope-area.open .envelope-hint {

    opacity: 0;

    pointer-events: none;

    transition:
        0.3s;
}


.letter-to {

    font-family:
        "Delius",
        cursive;

    font-size: 30px;

    margin-bottom: 22px;

    color: #733052;
}


.letter-text {

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 22px;

    line-height: 1.55;

    color: #5b2948;
}


.letter-sign {

    margin-top: 30px;

    text-align: right;

    font-family:
        "Delius",
        cursive;

    font-size: 27px;

    color: #733052;
}


/* =========================================================
   PAGE 6 - FINAL
========================================================= */

.final-page {

    justify-content: center;
}


.final-heart {

    position: relative;

    width: 125px;
    height: 125px;

    margin-bottom: 35px;

    transform:
        rotate(-45deg);

    background: #f19ac1;

    border-radius: 14px;

    box-shadow:
        0 0 35px rgba(255,160,210,0.55),
        0 0 80px rgba(255,140,205,0.25);

    animation:
        finalHeartbeat
        1.8s
        ease-in-out
        infinite;
}


.final-heart::before,
.final-heart::after {

    content: "";

    position: absolute;

    width: 125px;
    height: 125px;

    background: #f19ac1;

    border-radius: 50%;
}


.final-heart::before {

    top: -62px;
    left: 0;
}


.final-heart::after {

    top: 0;
    left: 62px;
}


@keyframes finalHeartbeat {

    0%,
    100% {

        transform:
            rotate(-45deg)
            scale(1);
    }

    50% {

        transform:
            rotate(-45deg)
            scale(1.08);
    }
}


.final-title {

    font-family:
        "Delius",
        cursive;

    font-size: 48px;

    line-height: 1.1;

    color: white;

    text-shadow:
        0 4px 15px rgba(0,0,0,0.25);
}


.final-name {

    margin-top: 10px;

    font-family:
        "Delius",
        cursive;

    font-size: 31px;

    color: #ffd9ea;
}


/* =========================================================
   FINAL CONFETTI
========================================================= */

.confetti-box {

    position: fixed;

    inset: 0;

    pointer-events: none;

    overflow: hidden;

    z-index: 8000;
}


.confetti {

    position: absolute;

    width: 7px;
    height: 13px;

    top: -20px;

    opacity: 0;

    animation:
        confettiFall
        2.5s
        linear
        forwards;
}


@keyframes confettiFall {

    0% {

        transform:
            translateY(0)
            rotate(0deg);

        opacity: 1;
    }

    100% {

        transform:
            translateY(110vh)
            rotate(720deg);

        opacity: 0.9;
    }
}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 700px) {

    .big-title {
        font-size: 34px;
    }

    .sub-title {
        font-size: 19px;
    }

    .photo-container {
        gap: 8px;
    }

    .photo-card {
        width: 29vw;
        max-width: 180px;
        padding: 6px 6px 12px;
    }

    .photo-card img {
        height: 28vw;
        max-height: 180px;
    }

    .photo-caption {
        font-size: 15px;
    }

    .letter {
        min-height: 500px;
        padding: 30px 25px;
    }

    .letter-text {
        font-size: 19px;
    }

    .letter-to {
        font-size: 27px;
    }

    .letter-sign {
        font-size: 24px;
    }
}

</style>
</head>


<body>

<div class="app">


<!-- =====================================================
     MOVING SPARKLES
===================================================== -->

<div class="sparkle"
     style="top:8%;left:15%;--moveX:35px;--moveY:25px;--duration:4s;--delay:0s;"></div>

<div class="sparkle"
     style="top:14%;left:47%;--moveX:-25px;--moveY:35px;--duration:5s;--delay:1s;"></div>

<div class="sparkle"
     style="top:20%;left:78%;--moveX:30px;--moveY:-25px;--duration:4.5s;--delay:0.5s;"></div>

<div class="sparkle"
     style="top:34%;left:10%;--moveX:-20px;--moveY:30px;--duration:5.5s;--delay:1.2s;"></div>

<div class="sparkle"
     style="top:40%;left:89%;--moveX:25px;--moveY:20px;--duration:4s;--delay:2s;"></div>

<div class="sparkle"
     style="top:53%;left:22%;--moveX:35px;--moveY:-30px;--duration:5s;--delay:0.7s;"></div>

<div class="sparkle"
     style="top:61%;left:73%;--moveX:-35px;--moveY:25px;--duration:4.5s;--delay:1.5s;"></div>

<div class="sparkle"
     style="top:75%;left:12%;--moveX:25px;--moveY:-20px;--duration:5.5s;--delay:2.2s;"></div>

<div class="sparkle"
     style="top:82%;left:48%;--moveX:-30px;--moveY:-30px;--duration:4.2s;--delay:0.8s;"></div>

<div class="sparkle"
     style="top:88%;left:82%;--moveX:30px;--moveY:-25px;--duration:5s;--delay:1.8s;"></div>

<div class="sparkle"
     style="top:27%;left:58%;--moveX:20px;--moveY:30px;--duration:4.8s;--delay:2.4s;"></div>

<div class="sparkle"
     style="top:68%;left:92%;--moveX:-25px;--moveY:-30px;--duration:5.2s;--delay:0.4s;"></div>


<!-- =====================================================
     PAGE 1
===================================================== -->

<section class="page active first-heart-page"
         id="page1">

    <div class="small-title">
        First things first
    </div>

    <div class="first-heart-area">

        <div class="start-heart"
             id="startHeart">
        </div>

        <div class="arrow"
             id="startArrow"
             onclick="startSurprise()">
        </div>

    </div>

    <div class="sub-title">
        Something special is waiting...
    </div>

</section>


<!-- =====================================================
     PAGE 2 - CAKE
===================================================== -->

<section class="page cake-page"
         id="page2">

    <div class="cake-area"
         id="cakeArea">

        <div class="plate"></div>

        <div class="cake-layer layer3"></div>

        <div class="cake-layer layer2"></div>

        <div class="cake-layer layer1"></div>

        <div class="cream cream1"></div>

        <div class="cream cream2"></div>

        <div class="cream cream3"></div>

        <div class="candle"></div>

        <div class="flame"></div>

        <div class="cake-message"
             id="cakeMessage">
            Happy Birthday Ricky!
        </div>

    </div>

    <button class="next-btn"
            onclick="goToPage(3)">
        Next
    </button>

</section>


<!-- =====================================================
     PAGE 3 - BALLOONS
===================================================== -->

<section class="page balloon-page"
         id="page3">

    <div class="balloon-title">
        Pop the balloons
    </div>

    <div class="balloon-area">

        <div class="balloon b1"
             onclick="popBalloon(this, 1)">
        </div>

        <div class="balloon b2"
             onclick="popBalloon(this, 2)">
        </div>

        <div class="balloon b3"
             onclick="popBalloon(this, 3)">
        </div>

        <div class="balloon b4"
             onclick="popBalloon(this, 4)">
        </div>

        <div class="balloon-message"
             id="balloonMessage">
        </div>

    </div>

    <button class="next-btn"
            onclick="goToPage(4)">
        Next
    </button>

</section>


<!-- =====================================================
     PAGE 4 - PHOTOS
===================================================== -->

<section class="page"
         id="page4">

    <div class="memory-title">
        A walk down memory lane
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

    <button class="next-btn"
            onclick="goToPage(5)">
        Next
    </button>

</section>


<!-- =====================================================
     PAGE 5 - ENVELOPE
===================================================== -->

<section class="page envelope-page"
         id="page5">

    <div class="envelope-area"
         id="envelopeArea"
         onclick="openEnvelope()">

        <div class="envelope"></div>

        <div class="envelope-flap"></div>

        <div class="seal"></div>

        <div class="envelope-hint">
            A little something for you...
        </div>


        <!-- FULL LETTER -->

        <div class="letter">

            <div class="letter-to">
                To my Ricky,
            </div>

            <div class="letter-text">

                Today is your special day, and I just wanted
                to leave a few words for you.

                <br><br>

                You are someone who has become very special
                to me. The little moments, the conversations,
                the smiles and even the simplest memories
                with you mean more to me than you may know.

                <br><br>

                I hope this new year of your life brings you
                lots of happiness, peace, success and beautiful
                moments.

                <br><br>

                No matter where life takes us, I hope you
                always remember that there is someone who
                genuinely wishes the very best for you.

                <br><br>

                Keep smiling, keep being yourself, and have
                the most beautiful birthday.

            </div>

            <div class="letter-sign">
                With lots of love,<br>
                From your Maggi
            </div>

        </div>

    </div>


    <button class="next-btn"
            id="letterNext"
            onclick="goToPage(6)"
            style="display:none;">
        Next
    </button>

</section>


<!-- =====================================================
     PAGE 6 - FINAL
===================================================== -->

<section class="page final-page"
         id="page6">

    <div class="final-heart"></div>

    <div class="final-title">
        HAPPY BIRTHDAY
    </div>

    <div class="final-name">
        Ricky!
    </div>

</section>


<!-- =====================================================
     EFFECT LAYERS
===================================================== -->

<div class="pink-flash"
     id="pinkFlash">
</div>

<div class="confetti-box"
     id="confettiBox">
</div>


</div>


<script>

/* =========================================================
   PAGE NAVIGATION
========================================================= */

function goToPage(pageNumber) {

    const pages =
        document.querySelectorAll(".page");

    pages.forEach(function(page) {
        page.classList.remove("active");
    });

    const selected =
        document.getElementById(
            "page" + pageNumber
        );

    if (selected) {
        selected.classList.add("active");
    }


    /* cake starts building */

    if (pageNumber === 2) {

        const cake =
            document.getElementById("cakeArea");

        cake.classList.remove("build");

        void cake.offsetWidth;

        cake.classList.add("build");

        const message =
            document.getElementById("cakeMessage");

        message.classList.remove("show");

        void message.offsetWidth;

        message.classList.add("show");
    }


    /* final confetti */

    if (pageNumber === 6) {

        createConfetti();
    }
}


/* =========================================================
   START HEART
========================================================= */

function startSurprise() {

    const arrow =
        document.getElementById("startArrow");

    const heart =
        document.getElementById("startHeart");

    const flash =
        document.getElementById("pinkFlash");


    /* arrow moves towards heart */

    arrow.classList.add("shoot");


    /* wait until arrow reaches heart */

    setTimeout(function() {

        heart.classList.add("blast");

        flash.classList.add("show");

        createPinkParticles();

    }, 650);


    /* move to cake */

    setTimeout(function() {

        goToPage(2);

    }, 1250);
}


/* =========================================================
   PINK PARTICLES
========================================================= */

function createPinkParticles() {

    for (
        let i = 0;
        i < 30;
        i++
    ) {

        const particle =
            document.createElement("div");

        particle.className =
            "particle";

        const angle =
            Math.random() *
            Math.PI * 2;

        const distance =
            120 +
            Math.random() * 330;

        particle.style.left =
            "50%";

        particle.style.top =
            "45%";

        particle.style.setProperty(
            "--x",
            Math.cos(angle) * distance + "px"
        );

        particle.style.setProperty(
            "--y",
            Math.sin(angle) * distance + "px"
        );

        document.body.appendChild(
            particle
        );

        setTimeout(function() {

            particle.remove();

        }, 1300);
    }
}


/* =========================================================
   BALLOON MESSAGES
========================================================= */

const balloonMessages = {

    1:
        "You make ordinary moments feel special.",

    2:
        "Your smile can make even a simple day brighter.",

    3:
        "I hope you always have reasons to smile.",

    4:
        "You are truly someone very special to me."
};


/* =========================================================
   POP BALLOON
========================================================= */

function popBalloon(balloon, number) {

    if (
        balloon.classList.contains("popped")
    ) {
        return;
    }

    balloon.classList.add("popped");


    const message =
        document.getElementById(
            "balloonMessage"
        );

    message.innerText =
        balloonMessages[number];

    message.classList.remove("show");

    void message.offsetWidth;

    message.classList.add("show");


    /* tiny pop particles */

    for (
        let i = 0;
        i < 10;
        i++
    ) {

        const particle =
            document.createElement("div");

        particle.className =
            "particle";

        const rect =
            balloon.getBoundingClientRect();

        particle.style.left =
            rect.left +
            rect.width / 2 +
            "px";

        particle.style.top =
            rect.top +
            rect.height / 2 +
            "px";

        const angle =
            Math.random() *
            Math.PI * 2;

        const distance =
            40 +
            Math.random() * 80;

        particle.style.setProperty(
            "--x",
            Math.cos(angle) * distance + "px"
        );

        particle.style.setProperty(
            "--y",
            Math.sin(angle) * distance + "px"
        );

        document.body.appendChild(
            particle
        );

        setTimeout(function() {

            particle.remove();

        }, 1200);
    }
}


/* =========================================================
   ENVELOPE OPEN
========================================================= */

function openEnvelope() {

    const envelope =
        document.getElementById(
            "envelopeArea"
        );

    if (
        envelope.classList.contains("open")
    ) {
        return;
    }

    envelope.classList.add("open");


    /* show next after letter opens */

    setTimeout(function() {

        const next =
            document.getElementById(
                "letterNext"
            );

        next.style.display =
            "inline-block";

    }, 1000);
}


/* =========================================================
   FINAL CONFETTI
========================================================= */

function createConfetti() {

    const box =
        document.getElementById(
            "confettiBox"
        );

    box.innerHTML = "";


    for (
        let i = 0;
        i < 65;
        i++
    ) {

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

        box.appendChild(piece);
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
# SHOW APP
# =========================================================

components.html(
    html,
    height=850,
    scrolling=False
)
