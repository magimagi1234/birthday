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

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Delius&display=swap" rel="stylesheet">

<style>

* {
    box-sizing: border-box;
}

html, body {
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
   MAIN SCREEN
===================================================== */

.app {
    width: 100%;
    height: 100vh;
    min-height: 700px;
    position: relative;
    overflow: hidden;

    background:
        radial-gradient(circle at 50% 40%,
        rgba(172, 74, 151, 0.45),
        transparent 45%),
        linear-gradient(
        180deg,
        #6d2865 0%,
        #42153f 55%,
        #2c0d2c 100%
        );

    color: white;
}


/* =====================================================
   SMALL STARS
===================================================== */

.star {
    position: absolute;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: rgba(255,255,255,0.85);
    box-shadow: 0 0 7px rgba(255,255,255,0.6);
}

.s1 { top: 9%; left: 22%; }
.s2 { top: 17%; left: 79%; }
.s3 { top: 32%; left: 12%; }
.s4 { top: 39%; right: 9%; }
.s5 { top: 58%; left: 19%; }
.s6 { top: 72%; right: 17%; }
.s7 { top: 84%; left: 35%; }
.s8 { top: 76%; right: 43%; }
.s9 { top: 23%; left: 49%; }


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
    color: #fff;
    text-shadow: 0 3px 10px rgba(0,0,0,0.25);
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

    background: linear-gradient(
        180deg,
        #f5a9cf,
        #df7fb1
    );

    color: white;

    font-family: "Patrick Hand", cursive;
    font-size: 20px;

    cursor: pointer;

    box-shadow:
        0 5px 16px rgba(0,0,0,0.25);

    transition: 0.25s;
}

.next-btn:hover {
    transform: scale(1.06);
}


/* =====================================================
   PAGE 1 - HEART + ARROW
===================================================== */

.first-heart-area {
    position: relative;
    width: 260px;
    height: 260px;

    margin-top: 5px;
}


/* heart shape */

.start-heart {
    position: absolute;

    width: 100px;
    height: 100px;

    left: 80px;
    top: 75px;

    background: #ef7fac;

    transform: rotate(-45deg);

    border-radius: 12px;

    box-shadow:
        0 0 30px rgba(255,133,181,0.45);

    cursor: pointer;

    transition: 0.25s;
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
    transform: rotate(-45deg) scale(1.08);
}


/* arrow */

.arrow {
    position: absolute;

    width: 120px;
    height: 6px;

    background: #6e243f;

    top: 105px;
    left: 115px;

    transform: rotate(-42deg);

    transform-origin: left center;

    border-radius: 10px;

    z-index: 10;

    animation: arrowFloat 1.5s infinite alternate;
}

.arrow:after {
    content: "";

    position: absolute;

    right: -2px;
    top: -7px;

    border-left: 18px solid #6e243f;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
}

@keyframes arrowFloat {
    from {
        transform: rotate(-42deg) translateX(0);
    }

    to {
        transform: rotate(-42deg) translateX(7px);
    }
}


/* =====================================================
   HEART BLAST
===================================================== */

.blast-heart {
    animation: heartBlast 0.65s forwards;
}

@keyframes heartBlast {
    0% {
        transform: rotate(-45deg) scale(1);
        opacity: 1;
    }

    50% {
        transform: rotate(-45deg) scale(1.5);
        opacity: 0.8;
    }

    100% {
        transform: rotate(-45deg) scale(0);
        opacity: 0;
    }
}

.pink-flash {
    position: fixed;

    inset: 0;

    background: #f49ac3;

    opacity: 0;

    pointer-events: none;

    z-index: 1000;
}

.pink-flash.show {
    animation: pinkSpread 1.1s forwards;
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

    z-index: 1001;

    animation: particleFly 1.2s ease-out forwards;
}

@keyframes particleFly {

    0% {
        transform: translate(0,0) scale(1);
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
   PAGE 2 - TREE
===================================================== */

.tree-area {
    position: relative;

    width: 330px;
    height: 390px;

    margin-top: -5px;
}


/* ground */

.tree-ground {
    position: absolute;

    width: 190px;
    height: 12px;

    left: 70px;
    bottom: 28px;

    background: rgba(20,5,20,0.25);

    border-radius: 50%;
}


/* trunk */

.tree-trunk {
    position: absolute;

    width: 19px;
    height: 245px;

    left: 156px;
    bottom: 35px;

    background: linear-gradient(
        90deg,
        #542030,
        #793146,
        #542030
    );

    border-radius: 10px;

    box-shadow:
        inset 3px 0 rgba(255,255,255,0.08);

    z-index: 2;
}


/* branches */

.branch {
    position: absolute;

    height: 12px;

    background: #60263b;

    border-radius: 12px;

    transform-origin: left center;

    z-index: 1;
}

.branch1 {
    width: 125px;

    left: 162px;
    bottom: 210px;

    transform: rotate(-35deg);
}

.branch2 {
    width: 120px;

    left: 158px;
    bottom: 175px;

    transform: rotate(31deg);
}

.branch3 {
    width: 115px;

    left: 156px;
    bottom: 135px;

    transform: rotate(-40deg);
}

.branch4 {
    width: 100px;

    left: 157px;
    bottom: 110px;

    transform: rotate(35deg);
}


/* little branches */

.branch1:after,
.branch2:after,
.branch3:after,
.branch4:after {
    content: "";

    position: absolute;

    width: 60px;
    height: 7px;

    background: #60263b;

    border-radius: 8px;

    top: 0;
}

.branch1:after {
    right: 15px;
    transform: rotate(35deg);
}

.branch2:after {
    right: 10px;
    transform: rotate(-40deg);
}

.branch3:after {
    right: 5px;
    transform: rotate(35deg);
}

.branch4:after {
    right: 0;
    transform: rotate(-35deg);
}


/* heart leaves */

.leaf {
    position: absolute;

    width: 37px;
    height: 37px;

    background: #f59bc2;

    transform: rotate(-45deg);

    border-radius: 8px;

    z-index: 5;

    filter:
        drop-shadow(0 3px 4px rgba(0,0,0,0.15));
}

.leaf:before,
.leaf:after {
    content: "";

    position: absolute;

    width: 37px;
    height: 37px;

    background: #f59bc2;

    border-radius: 50%;
}

.leaf:before {
    top: -18px;
    left: 0;
}

.leaf:after {
    left: 18px;
    top: 0;
}


/* leaf positions */

.l1 { left: 115px; top: 65px; }
.l2 { left: 160px; top: 78px; }
.l3 { left: 205px; top: 66px; }
.l4 { left: 91px; top: 115px; }
.l5 { left: 143px; top: 120px; }
.l6 { left: 197px; top: 112px; }
.l7 { left: 115px; top: 160px; }
.l8 { left: 170px; top: 157px; }
.l9 { left: 218px; top: 154px; }


/* =====================================================
   PAGE 3 - CAKE
===================================================== */

.cake-area {
    position: relative;

    width: 330px;
    height: 410px;

    margin-top: -10px;
}


/* cake plate */

.plate {
    position: absolute;

    width: 250px;
    height: 20px;

    bottom: 30px;
    left: 40px;

    border-radius: 50%;

    background: rgba(255,255,255,0.82);

    box-shadow:
        0 5px 10px rgba(0,0,0,0.2);
}


/* cake layers */

.cake-layer {
    position: absolute;

    left: 50%;

    transform: translateX(-50%);

    width: 205px;

    border-radius: 9px;

    background: linear-gradient(
        180deg,
        #f6b0cf,
        #dc7cae
    );

    box-shadow:
        0 7px 12px rgba(0,0,0,0.22);

    opacity: 0;
}


/* bottom layer */

.layer3 {
    height: 67px;

    bottom: 47px;

    width: 230px;
}


/* middle layer */

.layer2 {
    height: 62px;

    bottom: 105px;

    width: 195px;
}


/* top layer */

.layer1 {
    height: 55px;

    bottom: 158px;

    width: 155px;
}


/* cream */

.cream {
    position: absolute;

    left: 50%;

    transform: translateX(-50%);

    width: 145px;
    height: 14px;

    border-radius: 50%;

    background: #fff9fc;

    opacity: 0;

    z-index: 4;
}


/* positions */

.cream1 {
    bottom: 153px;
}

.cream2 {
    bottom: 100px;
    width: 184px;
}

.cream3 {
    bottom: 43px;
    width: 220px;
}


/* candle */

.candle {
    position: absolute;

    width: 19px;
    height: 75px;

    left: 50%;

    bottom: 213px;

    transform: translateX(-50%);

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


/* flame */

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
}


/* cake falling animations */

.cake-area.build .layer3 {
    animation: layerDrop 0.65s 0.2s forwards;
}

.cake-area.build .layer2 {
    animation: layerDrop 0.65s 0.9s forwards;
}

.cake-area.build .layer1 {
    animation: layerDrop 0.65s 1.6s forwards;
}

.cake-area.build .cream1 {
    animation: creamAppear 0.45s 2.15s forwards;
}

.cake-area.build .cream2 {
    animation: creamAppear 0.45s 2.45s forwards;
}

.cake-area.build .cream3 {
    animation: creamAppear 0.45s 2.75s forwards;
}

.cake-area.build .candle {
    animation: candleDrop 0.7s 3.1s forwards;
}

.cake-area.build .flame {
    animation:
        flameDrop 0.6s 3.55s forwards,
        flicker 0.8s 4.15s infinite alternate;
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


/* birthday text */

.cake-message {
    position: absolute;

    left: 50%;

    bottom: -10px;

    transform: translateX(-50%);

    width: 100%;

    font-family: "Delius", cursive;

    font-size: 36px;
    line-height: 1.15;

    color: white;

    opacity: 0;
}

.cake-message.show {
    animation: messageAppear 1s 4s forwards;
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
   PAGE 4 - BALLOONS
===================================================== */

.balloon-title {
    font-size: 25px;
    margin-bottom: 25px;
}


.balloon-area {
    width: 360px;
    height: 330px;

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

    background: rgba(255,255,255,0.65);

    top: 93px;
    left: 50%;
}


.balloon:before {
    content: "";

    position: absolute;

    bottom: -7px;
    left: 50%;

    transform: translateX(-50%);

    width: 0;
    height: 0;

    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 10px solid currentColor;
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
    transform: translateY(-5px) scale(1.05);
}


.balloon.popped {
    animation: popBalloon 0.35s forwards;
}


@keyframes popBalloon {

    0% {
        transform: scale(1);
        opacity: 1;
    }

    50% {
        transform: scale(1.3);
        opacity: 0.8;
    }

    100% {
        transform: scale(0);
        opacity: 0;
    }
}


/* balloon messages */

.balloon-message {
    position: absolute;

    width: 310px;

    left: 50%;
    bottom: 8px;

    transform: translateX(-50%) translateY(20px);

    font-size: 22px;

    color: #fff5fb;

    opacity: 0;

    transition: 0.4s;
}

.balloon-message.show {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}


/* =====================================================
   PAGE 5 - PHOTOS
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

    padding: 9px 9px 16px;

    background: #fff;

    border-radius: 4px;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.25);

    transform: rotate(-2deg);

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
   PAGE 6 - ENVELOPE
===================================================== */

.envelope-page {
    justify-content: center;
}


/* envelope wrapper */

.envelope-wrap {
    position: relative;

    width: 360px;
    height: 270px;

    display: flex;
    justify-content: center;
    align-items: center;
}


/* envelope */

.envelope {
    position: relative;

    width: 290px;
    height: 185px;

    background: #f5b3cf;

    border-radius: 8px;

    box-shadow:
        0 12px 25px rgba(0,0,0,0.25);

    cursor: pointer;

    transition: 0.6s;
}


.envelope:before {
    content: "";

    position: absolute;

    left: 0;
    top: 0;

    border-left: 145px solid transparent;
    border-right: 145px solid transparent;
    border-top: 100px solid #e892ba;

    z-index: 4;

    transform-origin: top center;

    transition: 0.7s;
}


/* lower folds */

.envelope:after {
    content: "";

    position: absolute;

    left: 0;
    bottom: 0;

    width: 0;
    height: 0;

    border-left: 145px solid #ef9fc3;
    border-top: 92px solid transparent;

    z-index: 3;
}


.envelope-letter {
    position: absolute;

    left: 22px;
    right: 22px;

    bottom: 8px;

    height: 150px;

    background: #fff7ed;

    color: #4b2943;

    padding: 22px 18px;

    border-radius: 5px;

    font-family: "Patrick Hand", cursive;

    font-size: 18px;

    line-height: 1.2;

    text-align: left;

    z-index: 2;

    transition: 0.7s;

    overflow: auto;
}


.envelope.open:before {
    transform: rotateX(180deg);
}


.envelope.open .envelope-letter {
    transform: translateY(-115px);

    z-index: 7;

    height: 235px;
}


.letter-title {
    text-align: center;

    font-family: "Delius", cursive;

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


/* envelope animation entering from side */

.envelope-wrap.enter {
    animation: envelopeEnter 1.3s ease-out forwards;
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
   PAGE 7 - FINAL
===================================================== */

.final-heart {
    position: relative;

    width: 120px;
    height: 120px;

    background: #e63f62;

    transform: rotate(-45deg);

    border-radius: 15px;

    margin-bottom: 40px;

    animation: heartBeat 1.2s infinite;
}

.final-heart:before,
.final-heart:after {
    content: "";

    position: absolute;

    width: 120px;
    height: 120px;

    background: #e63f62;

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


@keyframes heartBeat {

    0%,100% {
        transform: rotate(-45deg) scale(1);
    }

    50% {
        transform: rotate(-45deg) scale(1.08);
    }
}


.final-title {
    font-family: "Delius", cursive;

    font-size: 48px;

    line-height: 1.1;

    color: white;
}


.final-name {
    font-family: "Delius", cursive;

    font-size: 38px;

    margin-top: 5px;

    color: #f8b3d1;
}


/* =====================================================
   MOBILE
===================================================== */

@media (max-width: 600px) {

    .big-title {
        font-size: 34px;
    }

    .final-title {
        font-size: 38px;
    }

    .final-name {
        font-size: 31px;
    }

    .photo-container {
        gap: 8px;
    }

    .photo-card {
        width: 30%;
        padding: 5px 5px 10px;
    }

    .photo-card img {
        height: 170px;
    }

    .photo-caption {
        font-size: 14px;
    }

    .tree-area {
        transform: scale(0.85);
        margin-top: -20px;
    }

    .cake-area {
        transform: scale(0.82);
        margin-top: -35px;
    }

    .envelope-wrap {
        transform: scale(0.88);
    }
}

</style>
</head>


<body>

<div class="app">

    <!-- stars -->
    <div class="star s1"></div>
    <div class="star s2"></div>
    <div class="star s3"></div>
    <div class="star s4"></div>
    <div class="star s5"></div>
    <div class="star s6"></div>
    <div class="star s7"></div>
    <div class="star s8"></div>
    <div class="star s9"></div>


    <div class="pink-flash" id="pinkFlash"></div>


    <!-- =================================================
         PAGE 1
    ================================================== -->

    <section class="page active" id="page1">

        <div class="small-title">
            First things first
        </div>

        <div class="first-heart-area">

            <div class="arrow"></div>

            <div
                class="start-heart"
                id="startHeart"
                onclick="startSurprise()">
            </div>

        </div>

        <div class="big-title">
            A little surprise
        </div>

        <div class="sub-title">
            made just for you
        </div>

    </section>


    <!-- =================================================
         PAGE 2 - TREE
    ================================================== -->

    <section class="page" id="page2">

        <div class="small-title">
            Something special is growing...
        </div>

        <div class="tree-area">

            <div class="tree-ground"></div>

            <div class="tree-trunk"></div>

            <div class="branch branch1"></div>
            <div class="branch branch2"></div>
            <div class="branch branch3"></div>
            <div class="branch branch4"></div>

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

        <div class="big-title">
            A little tree<br>
            full of love
        </div>

        <button class="next-btn" onclick="showPage(3)">
            Next
        </button>

    </section>


    <!-- =================================================
         PAGE 3 - CAKE
    ================================================== -->

    <section class="page" id="page3">

        <div class="small-title">
            Something special is coming...
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

            <div class="cake-message" id="cakeMessage">
                HAPPY BIRTHDAY<br>
                RICKY
            </div>

        </div>

        <button class="next-btn" onclick="showPage(4)">
            Continue
        </button>

    </section>


    <!-- =================================================
         PAGE 4 - BALLOONS
    ================================================== -->

    <section class="page" id="page4">

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
            onclick="showPage(5)"
            style="opacity:0; pointer-events:none;">
            Continue
        </button>

    </section>


    <!-- =================================================
         PAGE 5 - PHOTOS
    ================================================== -->

    <section class="page" id="page5">

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

        <button class="next-btn" onclick="showPage(6)">
            Next
        </button>

    </section>


    <!-- =================================================
         PAGE 6 - ENVELOPE
    ================================================== -->

    <section class="page envelope-page" id="page6">

        <div class="small-title">
            One little letter for you
        </div>

        <div class="envelope-wrap" id="envelopeWrap">

            <div
                class="envelope"
                id="envelope"
                onclick="openEnvelope()">

                <div class="envelope-letter">

                    <div class="letter-title">
                        For you
                    </div>

                    <div>
                        You are someone very special to me.
                        Having you in my life makes even the
                        ordinary moments feel a little more beautiful.
                    </div>

                    <br>

                    <div>
                        I hope we always keep choosing each other,
                        supporting each other, and growing together.
                        If life gives us the chance to walk through
                        the future together, I would love for that
                        journey to be filled with understanding,
                        happiness and lots of little memories.
                    </div>

                    <br>

                    <div>
                        No matter where life takes us,
                        I will always be grateful for the beautiful
                        place you have in my heart.
                    </div>

                    <div class="from">
                        From your Maggi ♥
                    </div>

                </div>

            </div>

        </div>

        <button
            class="next-btn"
            id="letterNext"
            onclick="showPage(7)"
            style="opacity:0; pointer-events:none;">
            Next
        </button>

    </section>


    <!-- =================================================
         PAGE 7 - FINAL
    ================================================== -->

    <section class="page" id="page7">

        <div class="final-heart"></div>

        <div class="final-title">
            HAPPY BIRTHDAY
        </div>

        <div class="final-name">
            RICKY ♥
        </div>

    </section>


</div>


<script>

/* =====================================================
   PAGE CONTROL
===================================================== */

function showPage(number) {

    document.querySelectorAll(".page").forEach(function(page) {
        page.classList.remove("active");
    });

    const selected = document.getElementById("page" + number);

    if (selected) {
        selected.classList.add("active");
    }


    /* Cake animation */

    if (number === 3) {

        const cake = document.getElementById("cakeArea");

        cake.classList.remove("build");

        void cake.offsetWidth;

        cake.classList.add("build");

        setTimeout(function() {

            document
                .getElementById("cakeMessage")
                .classList.add("show");

            createConfetti(
                window.innerWidth / 2,
                window.innerHeight / 2 - 90,
                35
            );

        }, 3900);
    }


    /* Envelope enters from side but stops at CENTER */

    if (number === 6) {

        const wrap =
            document.getElementById("envelopeWrap");

        wrap.classList.remove("enter");

        void wrap.offsetWidth;

        wrap.classList.add("enter");
    }
}


/* =====================================================
   PAGE 1 HEART BLAST
===================================================== */

function startSurprise() {

    const heart =
        document.getElementById("startHeart");

    heart.classList.add("blast-heart");


    createHeartParticles(
        window.innerWidth / 2,
        window.innerHeight / 2,
        28
    );


    setTimeout(function() {

        document
            .getElementById("pinkFlash")
            .classList.add("show");

    }, 200);


    setTimeout(function() {

        showPage(2);

    }, 850);
}


/* =====================================================
   HEART PARTICLES
===================================================== */

function createHeartParticles(x, y, amount) {

    for (let i = 0; i < amount; i++) {

        const p = document.createElement("div");

        p.className = "particle";

        p.innerHTML = "♥";

        p.style.fontSize =
            (10 + Math.random() * 12) + "px";

        p.style.color =
            "#f49ac3";

        p.style.left = x + "px";
        p.style.top = y + "px";

        const angle =
            Math.random() * Math.PI * 2;

        const distance =
            70 + Math.random() * 220;

        p.style.setProperty(
            "--x",
            Math.cos(angle) * distance + "px"
        );

        p.style.setProperty(
            "--y",
            Math.sin(angle) * distance + "px"
        );

        document.body.appendChild(p);

        setTimeout(function() {
            p.remove();
        }, 1300);
    }
}


/* =====================================================
   CONFETTI
===================================================== */

function createConfetti(x, y, amount) {

    const colors = [
        "#f7a8c8",
        "#ffd1e3",
        "#b9d8f0",
        "#e9b2dd",
        "#fff2b8",
        "#ffffff"
    ];

    for (let i = 0; i < amount; i++) {

        const p = document.createElement("div");

        p.className = "particle";

        p.innerHTML = "■";

        p.style.color =
            colors[
                Math.floor(
                    Math.random() * colors.length
                )
            ];

        p.style.fontSize =
            (7 + Math.random() * 8) + "px";

        p.style.left = x + "px";
        p.style.top = y + "px";

        const angle =
            Math.random() * Math.PI * 2;

        const distance =
            80 + Math.random() * 260;

        p.style.setProperty(
            "--x",
            Math.cos(angle) * distance + "px"
        );

        p.style.setProperty(
            "--y",
            Math.sin(angle) * distance + "px"
        );

        document.body.appendChild(p);

        setTimeout(function() {
            p.remove();
        }, 1300);
    }
}


/* =====================================================
   BALLOON POP
===================================================== */

const balloonMessages = {

    1:
        "Your smile is one of my favourite things.",

    2:
        "You make ordinary moments feel special.",

    3:
        "I am really happy that you are a part of my life.",

    4:
        "Here is to many more beautiful memories together."
};


let poppedBalloons = 0;


function popBalloon(balloon, number) {

    if (balloon.classList.contains("popped")) {
        return;
    }

    balloon.classList.add("popped");

    poppedBalloons++;


    /* confetti exactly when balloon pops */

    const rect =
        balloon.getBoundingClientRect();

    createConfetti(
        rect.left + rect.width / 2,
        rect.top + rect.height / 2,
        22
    );


    const message =
        document.getElementById("balloonMessage");

    message.innerHTML =
        balloonMessages[number];

    message.classList.remove("show");

    void message.offsetWidth;

    message.classList.add("show");


    /* all balloons popped */

    if (poppedBalloons === 4) {

        setTimeout(function() {

            const next =
                document.getElementById("balloonNext");

            next.style.opacity = "1";
            next.style.pointerEvents = "auto";

        }, 600);
    }
}


/* =====================================================
   ENVELOPE
===================================================== */

let envelopeOpened = false;


function openEnvelope() {

    if (envelopeOpened) {
        return;
    }

    envelopeOpened = true;

    const envelope =
        document.getElementById("envelope");

    envelope.classList.add("open");


    /* tiny paper/confetti effect */

    const rect =
        envelope.getBoundingClientRect();

    createConfetti(
        rect.left + rect.width / 2,
        rect.top + 30,
        18
    );


    setTimeout(function() {

        const next =
            document.getElementById("letterNext");

        next.style.opacity = "1";
        next.style.pointerEvents = "auto";

    }, 850);
}

</script>

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
# SHOW APP
# ---------------------------------------------------------
components.html(
    html,
    height=850,
    scrolling=False
)
