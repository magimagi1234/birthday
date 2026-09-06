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

    background: #3d123d;
}


/* =====================================================
   MAIN APP
===================================================== */

.app {

    width: 100%;
    height: 100vh;

    min-height: 700px;

    position: relative;

    overflow: hidden;

    background:

        radial-gradient(
            circle at 50% 40%,
            rgba(172,74,151,0.45),
            transparent 45%
        ),

        linear-gradient(
            180deg,
            #6d2865 0%,
            #42153f 55%,
            #2c0d2c 100%
        );

    color: white;
}


/* =====================================================
   MOVING SPARKLES
===================================================== */

.sparkle {

    position: absolute;

    width: 4px;
    height: 4px;

    border-radius: 50%;

    background: rgba(255,255,255,0.9);

    box-shadow:
        0 0 8px rgba(255,255,255,0.9);

    pointer-events: none;

    animation:
        sparkleMove
        var(--duration)
        ease-in-out
        infinite;

    animation-delay: var(--delay);

    opacity: 0.4;
}


@keyframes sparkleMove {

    0% {

        transform:
            translate(
                0,
                0
            )
            scale(0.5);

        opacity: 0.15;
    }

    30% {

        opacity: 1;
    }

    50% {

        transform:
            translate(
                var(--moveX),
                var(--moveY)
            )
            scale(1.4);

        opacity: 1;
    }

    75% {

        opacity: 0.55;
    }

    100% {

        transform:
            translate(
                calc(var(--moveX) * -0.6),
                calc(var(--moveY) * -0.5)
            )
            scale(0.5);

        opacity: 0.15;
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
}


.page.active {

    display: flex;
}


/* =====================================================
   TEXT
===================================================== */

.small-title {

    font-size: 22px;

    letter-spacing: 1px;

    margin-bottom: 25px;

    color: #fff4fa;
}


.big-title {

    font-family: "Delius", cursive;

    font-size: 43px;

    line-height: 1.15;

    color: white;

    text-shadow:
        0 3px 10px rgba(0,0,0,0.25);
}


.sub-title {

    font-size: 23px;

    margin-top: 8px;

    color: #ffe7f3;
}


/* =====================================================
   BUTTON
===================================================== */

.next-btn {

    margin-top: 25px;

    border: none;

    outline: none;

    padding: 10px 27px;

    border-radius: 30px;

    background:
        linear-gradient(
            180deg,
            #f5a9cf,
            #df7fb1
        );

    color: white;

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 20px;

    cursor: pointer;

    box-shadow:
        0 5px 16px rgba(0,0,0,0.25);

    transition: 0.25s;
}


.next-btn:hover {

    transform:
        scale(1.06);
}


/* =====================================================
   PAGE 1 - HEART
===================================================== */

.first-heart-area {

    position: relative;

    width: 260px;

    height: 260px;

    margin-top: 5px;
}


.start-heart {

    position: absolute;

    width: 100px;
    height: 100px;

    left: 80px;
    top: 75px;

    background: #ef7fac;

    transform:
        rotate(-45deg);

    border-radius: 12px;

    box-shadow:
        0 0 30px rgba(255,133,181,0.45);

    cursor: pointer;

    transition: 0.25s;

    z-index: 5;
}


.start-heart:before,
.start-heart:after {

    content: "";

    position: absolute;

    width: 100px;
    height: 100px;

    background: #ef7fac;

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


.start-heart:hover {

    transform:
        rotate(-45deg)
        scale(1.08);
}


/* =====================================================
   ARROW
===================================================== */

.arrow {

    position: absolute;

    width: 120px;
    height: 6px;

    background: #6e243f;

    top: 105px;
    left: 115px;

    transform:
        rotate(-42deg);

    transform-origin: left center;

    border-radius: 10px;

    z-index: 10;

    animation:
        arrowFloat
        1.5s
        infinite
        alternate;
}


.arrow:after {

    content: "";

    position: absolute;

    right: -2px;
    top: -7px;

    border-left:
        18px solid #6e243f;

    border-top:
        10px solid transparent;

    border-bottom:
        10px solid transparent;
}


@keyframes arrowFloat {

    from {

        transform:
            rotate(-42deg)
            translateX(0);
    }

    to {

        transform:
            rotate(-42deg)
            translateX(7px);
    }
}


/* =====================================================
   HEART BLAST
===================================================== */

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

    50% {

        transform:
            rotate(-45deg)
            scale(1.5);

        opacity: 0.8;
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

    background: #f49ac3;

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
    }

    25% {
        opacity: 0.95;
    }

    100% {
        opacity: 0;
    }
}


/* =====================================================
   PARTICLES
===================================================== */

.particle {

    position: fixed;

    width: 8px;
    height: 8px;

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
            rotate(0deg)
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
            scale(0.2);

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

    margin-top: -10px;
}


.plate {

    position: absolute;

    width: 250px;
    height: 20px;

    bottom: 30px;
    left: 40px;

    border-radius: 50%;

    background:
        rgba(255,255,255,0.82);

    box-shadow:
        0 5px 10px rgba(0,0,0,0.2);
}


/* =====================================================
   CAKE LAYERS
===================================================== */

.cake-layer {

    position: absolute;

    left: 50%;

    transform:
        translateX(-50%);

    border-radius: 9px;

    background:
        linear-gradient(
            180deg,
            #f6b0cf,
            #dc7cae
        );

    box-shadow:
        0 7px 12px rgba(0,0,0,0.22);

    opacity: 0;
}


/* Bottom */

.layer3 {

    height: 67px;

    bottom: 47px;

    width: 230px;
}


/* Middle */

.layer2 {

    height: 62px;

    bottom: 105px;

    width: 195px;
}


/* Top */

.layer1 {

    height: 55px;

    bottom: 158px;

    width: 155px;
}


/* =====================================================
   CREAM
===================================================== */

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


/* =====================================================
   CANDLE
===================================================== */

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


/* =====================================================
   FLAME
===================================================== */

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
        0 0 15px #ffd67b;

    z-index: 7;
}


/* =====================================================
   CAKE FALLING
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


/* =====================================================
   LAYER DROP
===================================================== */

@keyframes layerDrop {

    0% {

        transform:
            translate(
                -50%,
                -280px
            )
            scale(0.9);

        opacity: 0;
    }

    70% {

        transform:
            translate(
                -50%,
                10px
            )
            scale(1.03);

        opacity: 1;
    }

    100% {

        transform:
            translate(
                -50%,
                0
            )
            scale(1);

        opacity: 1;
    }
}


/* =====================================================
   CREAM APPEAR
===================================================== */

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


/* =====================================================
   CANDLE DROP
===================================================== */

@keyframes candleDrop {

    0% {

        opacity: 0;

        transform:
            translate(
                -50%,
                -180px
            )
            rotate(-10deg);
    }

    75% {

        transform:
            translate(
                -50%,
                8px
            )
            rotate(4deg);
    }

    100% {

        opacity: 1;

        transform:
            translate(
                -50%,
                0
            )
            rotate(0);
    }
}


/* =====================================================
   FLAME
===================================================== */

@keyframes flameDrop {

    0% {

        opacity: 0;

        transform:
            translate(
                -50%,
                -150px
            )
            rotate(45deg);
    }

    100% {

        opacity: 1;

        transform:
            translate(
                -50%,
                0
            )
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
   CAKE MESSAGE
===================================================== */

.cake-message {

    position: absolute;

    left: 50%;

    bottom: -10px;

    transform:
        translateX(-50%);

    width: 100%;

    font-family:
        "Delius",
        cursive;

    font-size: 36px;

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
   CONFETTI
===================================================== */

.confetti-box {

    position: fixed;

    inset: 0;

    pointer-events: none;

    z-index: 5000;

    overflow: hidden;
}


.confetti {

    position: absolute;

    width: 8px;
    height: 13px;

    top: -20px;

    opacity: 0;

    animation:
        confettiFall
        2.2s
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
            translateY(105vh)
            rotate(720deg);

        opacity: 0.9;
    }
}


/* =====================================================
   PAGE 3 - BALLOONS
===================================================== */

.balloon-title {

    font-size: 25px;

    margin-bottom: 25px;
}


.balloon-area {

    width: 360px;

    height: 350px;

    position: relative;
}


/* =====================================================
   BALLOON
===================================================== */

.balloon {

    position: absolute;

    width: 75px;
    height: 95px;

    border-radius:
        50% 50% 45% 45%;

    cursor: pointer;

    transition: 0.15s;

    box-shadow:

        inset -12px -9px 18px
        rgba(0,0,0,0.13),

        inset 8px 5px 10px
        rgba(255,255,255,0.25);

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

    left: 40px;
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

    left: 225px;
    top: 48px;

    background: #a9c3dc;

    color: #a9c3dc;
}


.b4 {

    left: 128px;
    top: 125px;

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

        transform:
            scale(1);

        opacity: 1;
    }

    50% {

        transform:
            scale(1.3);

        opacity: 0.8;
    }

    100% {

        transform:
            scale(0);

        opacity: 0;
    }
}


/* =====================================================
   BALLOON MESSAGE
   TRANSPARENT PINK BOX
===================================================== */

.balloon-message {

    position: absolute;

    width: 320px;

    left: 50%;

    bottom: 5px;

    transform:
        translateX(-50%)
        translateY(20px);

    padding: 13px 18px;

    border-radius: 18px;

    background:
        rgba(245,158,198,0.30);

    border:
        1px solid
        rgba(255,220,238,0.38);

    box-shadow:
        0 5px 18px
        rgba(0,0,0,0.12);

    backdrop-filter:
        blur(3px);

    -webkit-backdrop-filter:
        blur(3px);

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


/* =====================================================
   PAGE 5 - ENVELOPE
===================================================== */

.envelope-page {

    justify-content: center;
}


.envelope-wrap {

    position: relative;

    width: 360px;

    height: 270px;

    display: flex;

    justify-content: center;

    align-items: center;
}


/* =====================================================
   ENVELOPE
===================================================== */

.envelope {

    position: relative;

    width: 290px;

    height: 185px;

    background: #f5b3cf;

    border-radius: 8px;

    box-shadow:
        0 12px 25px
        rgba(0,0,0,0.25);

    cursor: pointer;

    transition:
        0.4s;
}


.envelope:before {

    content: "";

    position: absolute;

    left: 0;
    top: 0;

    border-left:
        145px solid transparent;

    border-right:
        145px solid transparent;

    border-top:
        100px solid #e892ba;

    z-index: 4;

    transform-origin:
        top center;

    transition:
        0.7s;
}


/* lower fold */

.envelope:after {

    content: "";

    position: absolute;

    left: 0;

    bottom: 0;

    width: 0;
    height: 0;

    border-left:
        145px solid #ef9fc3;

    border-top:
        92px solid transparent;

    z-index: 3;
}


/* =====================================================
   SMALL LETTER PREVIEW
===================================================== */

.envelope-letter {

    position: absolute;

    left: 22px;
    right: 22px;

    bottom: 8px;

    height: 150px;

    background: #fff7ed;

    color: #4b2943;

    padding:
        22px 18px;

    border-radius: 5px;

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 18px;

    line-height: 1.2;

    text-align: left;

    z-index: 2;

    overflow: hidden;

    transition:
        0.5s;
}


.letter-title {

    text-align: center;

    font-family:
        "Delius",
        cursive;

    font-size: 24px;

    margin-bottom: 10px;

    color: #7b315c;
}


.from {

    text-align: right;

    margin-top: 13px;

    font-size: 21px;

    color: #8c3567;
}


/* =====================================================
   ENVELOPE ENTERS FROM SIDE
===================================================== */

.envelope-wrap.enter {

    animation:
        envelopeEnter
        1.3s
        ease-out
        forwards;
}


@keyframes envelopeEnter {

    from {

        transform:
            translateX(380px)
            scale(0.85);

        opacity: 0;
    }

    to {

        transform:
            translateX(0)
            scale(1);

        opacity: 1;
    }
}


/* =====================================================
   FULL LETTER OVERLAY
===================================================== */

.letter-overlay {

    position: fixed;

    inset: 0;

    display: none;

    align-items: center;

    justify-content: center;

    background:
        rgba(45,12,43,0.72);

    backdrop-filter:
        blur(5px);

    -webkit-backdrop-filter:
        blur(5px);

    z-index: 8000;

    padding: 25px;
}


.letter-overlay.show {

    display: flex;

    animation:
        overlayAppear
        0.45s
        ease-out
        forwards;
}


@keyframes overlayAppear {

    from {

        opacity: 0;
    }

    to {

        opacity: 1;
    }
}


/* =====================================================
   FULL LETTER
===================================================== */

.full-letter {

    width: min(520px, 92vw);

    max-height: 82vh;

    overflow-y: auto;

    background:
        linear-gradient(
            180deg,
            #fffaf2,
            #fff2df
        );

    color: #4b2943;

    border-radius: 8px;

    padding:
        30px 27px 25px;

    box-shadow:
        0 20px 60px
        rgba(0,0,0,0.45);

    text-align: left;

    transform:
        scale(0.75)
        translateY(35px);

    animation:
        letterOpen
        0.65s
        cubic-bezier(.17,.89,.32,1.28)
        forwards;
}


@keyframes letterOpen {

    to {

        transform:
            scale(1)
            translateY(0);
    }
}


.full-letter-title {

    text-align: center;

    font-family:
        "Delius",
        cursive;

    font-size: 31px;

    color: #7b315c;

    margin-bottom: 20px;
}


.full-letter-text {

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 21px;

    line-height: 1.42;

    color: #513344;
}


.full-letter-from {

    text-align: right;

    font-family:
        "Delius",
        cursive;

    font-size: 23px;

    color: #8c3567;

    margin-top: 25px;
}


/* close button */

.close-letter {

    display: block;

    margin:
        20px auto 0;

    border: none;

    border-radius: 25px;

    padding:
        8px 22px;

    background:
        linear-gradient(
            180deg,
            #f5a9cf,
            #df7fb1
        );

    color: white;

    font-family:
        "Patrick Hand",
        cursive;

    font-size: 18px;

    cursor: pointer;
}


/* =====================================================
   PAGE 6 - FINAL
===================================================== */

.final-heart {

    position: relative;

    width: 120px;

    height: 120px;

    margin-bottom: 25px;

    background:
        #ed6f9f;

    transform:
        rotate(-45deg);

    border-radius: 14px;

    box-shadow:
        0 0 35px
        rgba(255,118,168,0.5);

    animation:
        finalHeartPulse
        1.4s
        infinite
        alternate;
}


.final-heart:before,
.final-heart:after {

    content: "";

    position: absolute;

    width: 120px;
    height: 120px;

    background:
        #ed6f9f;

    border-radius: 50%;
}


.final-heart:before {

    top: -60px;
    left: 0;
}


.final-heart:after {

    top: 0;
    left: 60px;
}


@keyframes finalHeartPulse {

    from {

        transform:
            rotate(-45deg)
            scale(0.96);
    }

    to {

        transform:
            rotate(-45deg)
            scale(1.05);
    }
}


.final-title {

    font-family:
        "Delius",
        cursive;

    font-size: 46px;

    line-height: 1.15;

    color: white;

    text-shadow:
        0 4px 12px
        rgba(0,0,0,0.25);

    opacity: 0;
}


.final-title.show {

    animation:
        finalBirthday
        0.9s
        forwards;
}


@keyframes finalBirthday {

    from {

        opacity: 0;

        transform:
            translateY(25px)
            scale(0.8);
    }

    to {

        opacity: 1;

        transform:
            translateY(0)
            scale(1);
    }
}


/* =====================================================
   MOBILE
===================================================== */

@media (max-width: 700px) {

    .big-title {

        font-size: 36px;
    }

    .photo-container {

        gap: 8px;

        transform:
            scale(0.88);
    }

    .photo-card {

        width: 30vw;

        min-width: 100px;
    }

    .photo-card img {

        height: 160px;
    }

    .photo-caption {

        font-size: 15px;
    }

    .final-title {

        font-size: 38px;
    }

    .full-letter {

        padding:
            25px 20px;
    }

    .full-letter-text {

        font-size: 19px;
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
     style="top:8%;left:18%;--moveX:35px;--moveY:20px;--duration:4s;--delay:0s;"></div>

<div class="sparkle"
     style="top:15%;left:78%;--moveX:-30px;--moveY:25px;--duration:5s;--delay:1s;"></div>

<div class="sparkle"
     style="top:28%;left:10%;--moveX:25px;--moveY:-30px;--duration:4.5s;--delay:0.5s;"></div>

<div class="sparkle"
     style="top:35%;right:10%;--moveX:-35px;--moveY:20px;--duration:5.5s;--delay:2s;"></div>

<div class="sparkle"
     style="top:52%;left:20%;--moveX:30px;--moveY:-25px;--duration:4.2s;--delay:1.5s;"></div>

<div class="sparkle"
     style="top:68%;right:18%;--moveX:-25px;--moveY:-30px;--duration:5s;--delay:0.8s;"></div>

<div class="sparkle"
     style="top:82%;left:35%;--moveX:35px;--moveY:-20px;--duration:4.7s;--delay:2.5s;"></div>

<div class="sparkle"
     style="top:75%;right:42%;--moveX:-30px;--moveY:25px;--duration:5.3s;--delay:1.2s;"></div>

<div class="sparkle"
     style="top:22%;left:49%;--moveX:20px;--moveY:35px;--duration:4.4s;--delay:0.4s;"></div>

<div class="sparkle"
     style="top:47%;left:72%;--moveX:-25px;--moveY:-25px;--duration:5.8s;--delay:1.8s;"></div>

<div class="sparkle"
     style="top:88%;right:25%;--moveX:30px;--moveY:-25px;--duration:4.9s;--delay:2.2s;"></div>


<!-- =====================================================
     PINK FLASH
===================================================== -->

<div class="pink-flash" id="pinkFlash"></div>


<!-- =====================================================
     PAGE 1
===================================================== -->

<div class="page active" id="page1">

    <div class="small-title">
        First things first
    </div>

    <div class="first-heart-area">

        <div class="start-heart"
             id="startHeart"></div>

        <div class="arrow"></div>

    </div>

    <div class="sub-title">
        Something special is waiting...
    </div>

</div>


<!-- =====================================================
     PAGE 2 - CAKE
===================================================== -->

<div class="page" id="page2">

    <div class="small-title">
        Something special is coming...
    </div>

    <div class="cake-area" id="cakeArea">

        <div class="cake-layer layer3"></div>

        <div class="cream cream3"></div>

        <div class="cake-layer layer2"></div>

        <div class="cream cream2"></div>

        <div class="cake-layer layer1"></div>

        <div class="cream cream1"></div>

        <div class="candle"></div>

        <div class="flame"></div>

        <div class="plate"></div>

        <div class="cake-message"
             id="cakeMessage">

            HAPPY BIRTHDAY<br>
            RICKY

        </div>

    </div>

    <button class="next-btn"
            id="cakeNext"
            style="display:none;">

        Continue

    </button>

</div>


<!-- =====================================================
     PAGE 3 - BALLOONS
===================================================== -->

<div class="page" id="page3">

    <div class="balloon-title">
        Pop the balloons
    </div>

    <div class="balloon-area">

        <div class="balloon b1"
             data-message="You make ordinary moments feel special.">
        </div>

        <div class="balloon b2"
             data-message="I feel lucky to have you in my life.">
        </div>

        <div class="balloon b3"
             data-message="You are one of the people I never want to lose.">
        </div>

        <div class="balloon b4"
             data-message="I hope we keep making beautiful memories together.">
        </div>


        <div class="balloon-message"
             id="balloonMessage">
        </div>

    </div>

    <button class="next-btn"
            id="balloonNext"
            style="display:none;">

        Next

    </button>

</div>


<!-- =====================================================
     PAGE 4 - PHOTOS
===================================================== -->

<div class="page" id="page4">

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
            id="photoNext">

        Next

    </button>

</div>


<!-- =====================================================
     PAGE 5 - ENVELOPE
===================================================== -->

<div class="page envelope-page"
     id="page5">

    <div class="small-title">
        One little letter for you
    </div>


    <div class="envelope-wrap"
         id="envelopeWrap">

        <div class="envelope"
             id="envelope">

            <div class="envelope-letter">

                <div class="letter-title">
                    For You
                </div>

                Open this letter...

            </div>

        </div>

    </div>


    <button class="next-btn"
            id="envelopeNext"
            style="display:none;">

        Next

    </button>

</div>


<!-- =====================================================
     FULL LETTER OVERLAY
===================================================== -->

<div class="letter-overlay"
     id="letterOverlay">

    <div class="full-letter">

        <div class="full-letter-title">
            To Someone Special
        </div>


        <div class="full-letter-text">

            If I ever had to describe what I want
            from the person I choose to spend my
            life with, I would not ask for perfection.

            <br><br>

            I would want someone who understands
            me even when I don't say everything.
            Someone who stays during the ordinary
            days, celebrates the little things with me,
            and makes life feel a little warmer just
            by being there.

            <br><br>

            I want us to grow together, support each
            other, laugh at silly things, stand beside
            each other when life gets difficult, and
            create a life filled with small memories
            that mean more than anything.

            <br><br>

            And if someday you become the person
            I get to call my life partner, I hope you
            always know that I will value the little
            things too — your presence, your time,
            your kindness, and all those simple
            moments that make life beautiful.

            <br><br>

            I don't know exactly what the future
            will look like, but if I get to share it
            with you, I hope it is full of laughter,
            peace, understanding, and a lot of
            beautiful memories.

        </div>


        <div class="full-letter-from">
            From your Maggi
        </div>


        <button class="close-letter"
                id="closeLetter">

            Close

        </button>

    </div>

</div>


<!-- =====================================================
     PAGE 6 - FINAL
===================================================== -->

<div class="page" id="page6">

    <div class="final-heart"></div>

    <div class="final-title"
         id="finalTitle">

        HAPPY BIRTHDAY<br>
        RICKY

    </div>

</div>


<!-- =====================================================
     CONFETTI CONTAINER
===================================================== -->

<div class="confetti-box"
     id="confettiBox">
</div>


<script>

/* =====================================================
   PAGE SWITCH
===================================================== */

function showPage(number) {

    document
        .querySelectorAll(".page")
        .forEach(function(page) {

            page.classList.remove("active");

        });


    const target =
        document.getElementById(
            "page" + number
        );


    if (target) {

        target.classList.add("active");
    }
}


/* =====================================================
   PARTICLES
===================================================== */

function createParticles(
    count = 28,
    centerX = window.innerWidth / 2,
    centerY = window.innerHeight / 2
) {

    for (
        let i = 0;
        i < count;
        i++
    ) {

        const p =
            document.createElement("div");

        p.className =
            "particle";


        const angle =
            Math.random() *
            Math.PI *
            2;


        const distance =
            80 +
            Math.random() * 230;


        p.style.left =
            centerX + "px";


        p.style.top =
            centerY + "px";


        p.style.setProperty(
            "--x",
            Math.cos(angle) *
            distance +
            "px"
        );


        p.style.setProperty(
            "--y",
            Math.sin(angle) *
            distance +
            "px"
        );


        const shapes = [
            "50%",
            "2px",
            "0%"
        ];


        p.style.borderRadius =
            shapes[
                Math.floor(
                    Math.random() *
                    shapes.length
                )
            ];


        const size =
            5 +
            Math.random() * 7;


        p.style.width =
            size + "px";


        p.style.height =
            size + "px";


        const pinks = [
            "#ffd1e5",
            "#f59bc2",
            "#f7c2dc",
            "#ffffff",
            "#e7a9d4"
        ];


        p.style.background =
            pinks[
                Math.floor(
                    Math.random() *
                    pinks.length
                )
            ];


        document.body.appendChild(p);


        setTimeout(
            function() {

                p.remove();

            },
            1300
        );
    }
}


/* =====================================================
   CONFETTI
===================================================== */

function createConfetti(
    count = 70
) {

    const box =
        document.getElementById(
            "confettiBox"
        );


    const colors = [
        "#f7a8c8",
        "#f6d4e5",
        "#b9d5ed",
        "#e8b1dc",
        "#ffd58f",
        "#ffffff",
        "#d5b5e8"
    ];


    for (
        let i = 0;
        i < count;
        i++
    ) {

        const c =
            document.createElement("div");


        c.className =
            "confetti";


        c.style.left =
            Math.random() * 100 +
            "%";


        c.style.background =
            colors[
                Math.floor(
                    Math.random() *
                    colors.length
                )
            ];


        c.style.animationDelay =
            Math.random() * 0.6 +
            "s";


        c.style.animationDuration =
            1.7 +
            Math.random() * 1.2 +
            "s";


        c.style.transform =
            "rotate(" +
            Math.random() * 360 +
            "deg)";


        box.appendChild(c);


        setTimeout(
            function() {

                c.remove();

            },
            3500
        );
    }
}


/* =====================================================
   PAGE 1 HEART
===================================================== */

const startHeart =
    document.getElementById(
        "startHeart"
    );


const pinkFlash =
    document.getElementById(
        "pinkFlash"
    );


startHeart.addEventListener(
    "click",
    function() {

        if (
            startHeart.classList.contains(
                "blast-heart"
            )
        ) {
            return;
        }


        startHeart.classList.add(
            "blast-heart"
        );


        const rect =
            startHeart.getBoundingClientRect();


        createParticles(
            32,
            rect.left +
            rect.width / 2,
            rect.top +
            rect.height / 2
        );


        pinkFlash.classList.add(
            "show"
        );


        setTimeout(
            function() {

                showPage(2);

                startCake();

            },
            850
        );

    }
);


/* =====================================================
   CAKE
===================================================== */

let cakeStarted = false;


function startCake() {

    if (cakeStarted) {
        return;
    }

    cakeStarted = true;


    const cake =
        document.getElementById(
            "cakeArea"
        );


    cake.classList.add(
        "build"
    );


    const message =
        document.getElementById(
            "cakeMessage"
        );


    message.classList.add(
        "show"
    );


    /*
       Cake completes,
       then colourful paper pieces pop.
    */

    setTimeout(
        function() {

            createConfetti(65);


            const next =
                document.getElementById(
                    "cakeNext"
                );


            next.style.display =
                "inline-block";

        },
        5100
    );
}


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
    document.querySelectorAll(
        ".balloon"
    );


const balloonMessage =
    document.getElementById(
        "balloonMessage"
    );


const balloonNext =
    document.getElementById(
        "balloonNext"
    );


let poppedBalloons = 0;


balloons.forEach(
    function(balloon) {

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


                poppedBalloons++;


                const rect =
                    balloon.getBoundingClientRect();


                createParticles(
                    20,
                    rect.left +
                    rect.width / 2,
                    rect.top +
                    rect.height / 2
                );


                balloonMessage.textContent =
                    balloon.dataset.message;


                balloonMessage.classList.add(
                    "show"
                );


                if (
                    poppedBalloons ===
                    balloons.length
                ) {

                    setTimeout(
                        function() {

                            balloonNext.style.display =
                                "inline-block";

                        },
                        600
                    );
                }

            }
        );

    }
);


balloonNext.addEventListener(
    "click",
    function() {

        showPage(4);

    }
);


/* =====================================================
   PHOTOS
===================================================== */

document
    .getElementById("photoNext")
    .addEventListener(
        "click",
        function() {

            showPage(5);


            const wrap =
                document.getElementById(
                    "envelopeWrap"
                );


            wrap.classList.remove(
                "enter"
            );


            void wrap.offsetWidth;


            wrap.classList.add(
                "enter"
            );

        }
    );


/* =====================================================
   ENVELOPE
===================================================== */

const envelope =
    document.getElementById(
        "envelope"
    );


const letterOverlay =
    document.getElementById(
        "letterOverlay"
    );


envelope.addEventListener(
    "click",
    function() {

        /*
           Instead of pulling the letter
           halfway out of the envelope,
           open a completely separate
           full letter.
        */

        letterOverlay.classList.add(
            "show"
        );

    }
);


/* =====================================================
   CLOSE LETTER
===================================================== */

document
    .getElementById("closeLetter")
    .addEventListener(
        "click",
        function() {

            letterOverlay.classList.remove(
                "show"
            );


            setTimeout(
                function() {

                    showPage(6);

                    startFinal();

                },
                350
            );

        }
    );


/* =====================================================
   FINAL
===================================================== */

let finalStarted = false;


function startFinal() {

    if (finalStarted) {
        return;
    }


    finalStarted = true;


    const title =
        document.getElementById(
            "finalTitle"
        );


    setTimeout(
        function() {

            title.classList.add(
                "show"
            );


            /*
               Birthday text appears
               and colourful paper pieces
               pop from the screen.
            */

            setTimeout(
                function() {

                    createConfetti(
                        100
                    );

                    createParticles(
                        45
                    );

                },
                650
            );

        },
        500
    );
}


/* =====================================================
   PREVENT BACKDROP CLICK
   FROM CLOSING LETTER
===================================================== */

letterOverlay.addEventListener(
    "click",
    function(event) {

        if (
            event.target ===
            letterOverlay
        ) {

            letterOverlay.classList.remove(
                "show"
            );

            setTimeout(
                function() {

                    showPage(6);

                    startFinal();

                },
                350
            );
        }

    }
);

</script>

</div>

</body>
</html>
"""


# ---------------------------------------------------------
# INSERT PHOTOS
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# STREAMLIT DISPLAY
# ---------------------------------------------------------

components.html(
    html,
    height=850,
    scrolling=False
)
