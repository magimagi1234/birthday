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
   PAGE 2 - NEW TREE
===================================================== */

.tree-area {
    position: relative;

    width: 360px;
    height: 430px;

    margin-top: -5px;
}


/* ground */

.tree-ground {
    position: absolute;

    width: 215px;
    height: 15px;

    left: 72px;
    bottom: 24px;

    background: rgba(15,3,15,0.28);

    border-radius: 50%;

    filter: blur(1px);
}


/* -----------------------------------------------------
   MAIN TRUNK
----------------------------------------------------- */

.tree-trunk {
    position: absolute;

    width: 20px;
    height: 270px;

    left: 170px;
    bottom: 34px;

    background:
        linear-gradient(
            90deg,
            #4d1c2c 0%,
            #6c293d 35%,
            #81364d 55%,
            #572031 100%
        );

    border-radius: 12px;

    transform-origin: bottom center;

    z-index: 2;

    animation: treeGrow 1.4s ease-out forwards;
}

@keyframes treeGrow {

    0% {
        transform: scaleY(0);
        opacity: 0;
    }

    100% {
        transform: scaleY(1);
        opacity: 1;
    }
}


/* -----------------------------------------------------
   BRANCHES
----------------------------------------------------- */

.tree-branch {
    position: absolute;

    height: 11px;

    background:
        linear-gradient(
            90deg,
            #552031,
            #713047,
            #5a2336
        );

    border-radius: 12px;

    transform-origin: left center;

    z-index: 1;

    opacity: 0;

    animation:
        branchGrow 0.9s ease-out forwards;
}

.branch-a {
    width: 135px;
    left: 174px;
    bottom: 220px;
    transform: rotate(-34deg);
    animation-delay: 0.9s;
}

.branch-b {
    width: 125px;
    left: 170px;
    bottom: 180px;
    transform: rotate(34deg);
    animation-delay: 1.15s;
}

.branch-c {
    width: 128px;
    left: 169px;
    bottom: 145px;
    transform: rotate(-38deg);
    animation-delay: 1.4s;
}

.branch-d {
    width: 112px;
    left: 170px;
    bottom: 110px;
    transform: rotate(36deg);
    animation-delay: 1.65s;
}

.branch-e {
    width: 95px;
    left: 171px;
    bottom: 255px;
    transform: rotate(24deg);
    animation-delay: 1.9s;
}

@keyframes branchGrow {

    0% {
        transform:
            rotate(var(--angle))
            scaleX(0);
        opacity: 0;
    }

    100% {
        transform:
            rotate(var(--angle))
            scaleX(1);
        opacity: 1;
    }
}


/* -----------------------------------------------------
   SMALL TWIGS
----------------------------------------------------- */

.twig {
    position: absolute;

    width: 65px;
    height: 6px;

    background: #60263b;

    border-radius: 8px;

    transform-origin: left center;

    z-index: 1;

    opacity: 0;

    animation: twigAppear 0.7s ease-out forwards;
}

.twig1 {
    left: 248px;
    bottom: 245px;
    transform: rotate(-55deg);
    animation-delay: 2.0s;
}

.twig2 {
    left: 245px;
    bottom: 205px;
    transform: rotate(55deg);
    animation-delay: 2.15s;
}

.twig3 {
    left: 245px;
    bottom: 165px;
    transform: rotate(-58deg);
    animation-delay: 2.3s;
}

.twig4 {
    left: 240px;
    bottom: 128px;
    transform: rotate(55deg);
    animation-delay: 2.45s;
}

.twig5 {
    left: 108px;
    bottom: 235px;
    transform: rotate(38deg);
    animation-delay: 2.1s;
}

.twig6 {
    left: 105px;
    bottom: 195px;
    transform: rotate(-48deg);
    animation-delay: 2.25s;
}

.twig7 {
    left: 112px;
    bottom: 155px;
    transform: rotate(45deg);
    animation-delay: 2.4s;
}

@keyframes twigAppear {

    0% {
        transform:
            rotate(0deg)
            scaleX(0);
        opacity: 0;
    }

    100% {
        opacity: 1;
    }
}


/* -----------------------------------------------------
   HEART LEAVES
----------------------------------------------------- */

.tree-heart {
    position: absolute;

    width: 27px;
    height: 27px;

    background: #f39bc2;

    transform: rotate(-45deg) scale(0);

    border-radius: 6px;

    z-index: 5;

    opacity: 0;

    filter:
        drop-shadow(
            0 3px 5px rgba(0,0,0,0.20)
        );

    animation:
        heartLeafAppear 0.55s
        cubic-bezier(.17,.89,.32,1.49)
        forwards;
}

.tree-heart:before,
.tree-heart:after {
    content: "";

    position: absolute;

    width: 27px;
    height: 27px;

    background: #f39bc2;

    border-radius: 50%;
}

.tree-heart:before {
    top: -13px;
    left: 0;
}

.tree-heart:after {
    top: 0;
    left: 13px;
}

@keyframes heartLeafAppear {

    0% {
        opacity: 0;
        transform:
            rotate(-45deg)
            scale(0);
    }

    70% {
        opacity: 1;
        transform:
            rotate(-45deg)
            scale(1.18);
    }

    100% {
        opacity: 1;
        transform:
            rotate(-45deg)
            scale(1);
    }
}


/* many heart positions */

.h1  { left: 145px; top: 52px;  animation-delay: 2.3s; }
.h2  { left: 185px; top: 58px;  animation-delay: 2.45s; }
.h3  { left: 225px; top: 72px;  animation-delay: 2.6s; }

.h4  { left: 118px; top: 82px;  animation-delay: 2.55s; }
.h5  { left: 158px; top: 91px;  animation-delay: 2.7s; }
.h6  { left: 205px; top: 98px;  animation-delay: 2.85s; }
.h7  { left: 245px; top: 105px; animation-delay: 3s; }

.h8  { left: 98px;  top: 120px; animation-delay: 2.8s; }
.h9  { left: 137px; top: 126px; animation-delay: 2.95s; }
.h10 { left: 180px; top: 133px; animation-delay: 3.1s; }
.h11 { left: 225px; top: 140px; animation-delay: 3.25s; }
.h12 { left: 260px; top: 145px; animation-delay: 3.4s; }

.h13 { left: 112px; top: 165px; animation-delay: 3.15s; }
.h14 { left: 151px; top: 170px; animation-delay: 3.3s; }
.h15 { left: 198px; top: 177px; animation-delay: 3.45s; }
.h16 { left: 239px; top: 180px; animation-delay: 3.6s; }

.h17 { left: 132px; top: 205px; animation-delay: 3.45s; }
.h18 { left: 175px; top: 210px; animation-delay: 3.6s; }
.h19 { left: 218px; top: 214px; animation-delay: 3.75s; }

.h20 { left: 150px; top: 242px; animation-delay: 3.65s; }
.h21 { left: 190px; top: 245px; animation-delay: 3.8s; }
.h22 { left: 230px; top: 240px; animation-delay: 3.95s; }


/* slightly different sizes */

.h2, .h6, .h10, .h15, .h19 {
    width: 22px;
    height: 22px;
}

.h2:before,
.h2:after,
.h6:before,
.h6:after,
.h10:before,
.h10:after,
.h15:before,
.h15:after,
.h19:before,
.h19:after {
    width: 22px;
    height: 22px;
}

.h2:before,
.h6:before,
.h10:before,
.h15:before,
.h19:before {
    top: -11px;
}

.h2:after,
.h6:after,
.h10:after,
.h15:after,
.h19:after {
    left: 11px;
}


/* tree title */

.tree-title {
    font-family: "Delius", cursive;

    font-size: 37px;

    line-height: 1.15;

    margin-top: 5px;

    color: #fff;

    text-shadow:
        0 3px 10px rgba(0,0,0,0.25);
}


/* =====================================================
   PAGE 3 - CAKE
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

    background: rgba(255,255,255,0.82);

    box-shadow:
        0 5px 10px rgba(0,0,0,0.2);
}

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

    transform: translateX(-50%);

    width: 145px;
    height: 14px;

    border-radius: 50%;

    background: #fff9fc;

    opacity: 0;

    z-index: 4;
}

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


/* cake animation */

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
   CONFETTI
===================================================== */

.confetti-box {
    position: fixed;
    inset: 0;

    pointer-events: none;

    z-index: 2000;

    overflow: hidden;
}

.confetti {
    position: absolute;

    width: 8px;
    height: 13px;

    top: -20px;

    opacity: 0;

    animation: confettiFall 2.2s linear forwards;
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

.balloon-message {
    position: absolute;

    width: 310px;

    left: 50%;
    bottom: 8px;

    transform:
        translateX(-50%)
        translateY(20px);

    font-size: 22px;

    color: #fff5fb;

    opacity: 0;

    transition: 0.4s;
}

.balloon-message.show {
    opacity: 1;

    transform:
        translateX(-50%)
        translateY(0);
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

.envelope-wrap {
    position: relative;

    width: 360px;
    height: 270px;

    display: flex;
    justify-content: center;
    align-items: center;
}

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
   FINAL PAGE
===================================================== */

.final-heart {
    position: relative;

    width: 125px;
    height: 125px;

    background: #ef7fac;

    transform: rotate(-45deg);

    border-radius: 15px;

    box-shadow:
        0 0 35px rgba(255,140,190,0.55);

    animation: finalHeartBeat 1.2s infinite;
}

.final-heart:before,
.final-heart:after {
    content: "";

    position: absolute;

    width: 125px;
    height: 125px;

    background: #ef7fac;

    border-radius: 50%;
}

.final-heart:before {
    top: -62px;
    left: 0;
}

.final-heart:after {
    left: 62px;
    top: 0;
}

@keyframes finalHeartBeat {

    0%, 100% {
        transform: rotate(-45deg) scale(1);
    }

    50% {
        transform: rotate(-45deg) scale(1.08);
    }
}

.final-text {
    font-family: "Delius", cursive;

    font-size: 42px;

    line-height: 1.1;

    margin-top: 55px;

    color: white;

    text-shadow:
        0 3px 12px rgba(0,0,0,0.25);
}


/* =====================================================
   MOBILE
===================================================== */

@media (max-width: 600px) {

    .big-title {
        font-size: 35px;
    }

    .tree-area {
        transform: scale(0.88);
        transform-origin: center;
        margin-bottom: -35px;
    }

    .cake-area {
        transform: scale(0.9);
        transform-origin: center;
    }

    .photo-container {
        transform: scale(0.8);
        gap: 8px;
    }

    .photo-card {
        width: 180px;
    }

    .photo-card img {
        height: 190px;
    }

    .envelope {
        width: 275px;
    }

    .final-text {
        font-size: 34px;
    }
}

</style>
</head>


<body>

<div class="app">

    <div class="star s1"></div>
    <div class="star s2"></div>
    <div class="star s3"></div>
    <div class="star s4"></div>
    <div class="star s5"></div>
    <div class="star s6"></div>
    <div class="star s7"></div>
    <div class="star s8"></div>
    <div class="star s9"></div>


    <!-- =================================================
         PAGE 1
    ================================================== -->

    <section class="page active" id="page1">

        <div class="small-title">
            First things first
        </div>

        <div class="first-heart-area">

            <div class="start-heart" id="startHeart"></div>

            <div class="arrow"></div>

        </div>

        <div class="sub-title">
            Something special is waiting...
        </div>

    </section>


    <!-- =================================================
         PAGE 2 - TREE
    ================================================== -->

    <section class="page" id="page2">

        <div class="small-title">
            A little tree
        </div>

        <div class="tree-area">

            <div class="tree-ground"></div>

            <div class="tree-trunk"></div>

            <div class="tree-branch branch-a"></div>
            <div class="tree-branch branch-b"></div>
            <div class="tree-branch branch-c"></div>
            <div class="tree-branch branch-d"></div>
            <div class="tree-branch branch-e"></div>

            <div class="twig twig1"></div>
            <div class="twig twig2"></div>
            <div class="twig twig3"></div>
            <div class="twig twig4"></div>
            <div class="twig twig5"></div>
            <div class="twig twig6"></div>
            <div class="twig twig7"></div>


            <!-- MANY HEART LEAVES -->

            <div class="tree-heart h1"></div>
            <div class="tree-heart h2"></div>
            <div class="tree-heart h3"></div>
            <div class="tree-heart h4"></div>
            <div class="tree-heart h5"></div>
            <div class="tree-heart h6"></div>
            <div class="tree-heart h7"></div>
            <div class="tree-heart h8"></div>
            <div class="tree-heart h9"></div>
            <div class="tree-heart h10"></div>
            <div class="tree-heart h11"></div>
            <div class="tree-heart h12"></div>
            <div class="tree-heart h13"></div>
            <div class="tree-heart h14"></div>
            <div class="tree-heart h15"></div>
            <div class="tree-heart h16"></div>
            <div class="tree-heart h17"></div>
            <div class="tree-heart h18"></div>
            <div class="tree-heart h19"></div>
            <div class="tree-heart h20"></div>
            <div class="tree-heart h21"></div>
            <div class="tree-heart h22"></div>

        </div>

        <div class="tree-title">
            A little tree<br>
            full of love
        </div>

        <button class="next-btn" onclick="goToPage(3)">
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

            <div class="cake-message">
                HAPPY BIRTHDAY<br>
                RICKY
            </div>

        </div>

        <button class="next-btn" onclick="goToPage(4)">
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

            <div class="balloon b1"
                 onclick="popBalloon(this, 'You make ordinary moments feel special.')">
            </div>

            <div class="balloon b2"
                 onclick="popBalloon(this, 'I am really grateful for you.')">
            </div>

            <div class="balloon b3"
                 onclick="popBalloon(this, 'Some people simply become important to your heart.')">
            </div>

            <div class="balloon b4"
                 onclick="popBalloon(this, 'You are one of those people for me.')">
            </div>

            <div class="balloon-message" id="balloonMessage"></div>

        </div>

        <button class="next-btn" onclick="goToPage(5)">
            Next
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

        <button class="next-btn" onclick="goToPage(6)">
            Next
        </button>

    </section>


    <!-- =================================================
         PAGE 6 - ENVELOPE
    ================================================== -->

    <section class="page envelope-page" id="page6">

        <div class="small-title">
            A little letter for you
        </div>

        <div class="envelope-wrap" id="envelopeWrap">

            <div class="envelope" id="envelope"
                 onclick="openEnvelope()">

                <div class="envelope-letter">

                    <div class="letter-title">
                        To Ricky
                    </div>

                    If life ever gives us the chance to walk
                    through many more years together, I hope
                    we keep choosing each other through every
                    happy moment, every difficult day, and
                    every little thing in between.

                    <br><br>

                    I don't know what the future has written
                    for us, but if someday you become my life
                    partner, I would want our life to be filled
                    with friendship, understanding, laughter,
                    respect and a lot of love.

                    <br><br>

                    Until then, I just want you to know that
                    you are someone very special to me.

                    <div class="from">
                        From your Maggi ♥
                    </div>

                </div>

            </div>

        </div>

        <button class="next-btn" onclick="goToPage(7)">
            Next
        </button>

    </section>


    <!-- =================================================
         PAGE 7 - FINAL
    ================================================== -->

    <section class="page" id="page7">

        <div class="final-heart"></div>

        <div class="final-text">
            HAPPY BIRTHDAY<br>
            RICKY
        </div>

        <button class="next-btn" onclick="finalPop()">
            ♥
        </button>

    </section>


    <!-- =================================================
         FLASH + CONFETTI
    ================================================== -->

    <div class="pink-flash" id="pinkFlash"></div>

    <div class="confetti-box" id="confettiBox"></div>

</div>


<script>


/* =====================================================
   PAGE NAVIGATION
===================================================== */

function goToPage(number) {

    document.querySelectorAll(".page").forEach(function(page) {
        page.classList.remove("active");
    });

    const nextPage = document.getElementById("page" + number);

    if (nextPage) {
        nextPage.classList.add("active");
    }


    /* Tree animation starts fresh */

    if (number === 2) {

        const hearts =
            document.querySelectorAll(".tree-heart");

        hearts.forEach(function(heart) {

            heart.style.animation = "none";

            void heart.offsetWidth;

            heart.style.animation = "";

        });

    }


    /* Cake animation */

    if (number === 3) {

        const cake =
            document.getElementById("cakeArea");

        cake.classList.remove("build");

        void cake.offsetWidth;

        cake.classList.add("build");

        setTimeout(function() {

            document
                .querySelector(".cake-message")
                .classList.add("show");

        }, 50);

    }


    /* Envelope comes to middle */

    if (number === 6) {

        const wrap =
            document.getElementById("envelopeWrap");

        wrap.classList.remove("enter");

        void wrap.offsetWidth;

        wrap.classList.add("enter");

    }

}


/* =====================================================
   START HEART
===================================================== */

document
    .getElementById("startHeart")
    .addEventListener("click", function() {

        const heart = this;

        heart.classList.add("blast-heart");

        createParticles(
            window.innerWidth / 2,
            window.innerHeight / 2,
            25
        );

        document
            .getElementById("pinkFlash")
            .classList.add("show");


        setTimeout(function() {

            goToPage(2);

        }, 850);

    });


/* =====================================================
   PARTICLES
===================================================== */

function createParticles(x, y, amount) {

    for (let i = 0; i < amount; i++) {

        const particle =
            document.createElement("div");

        particle.className = "particle";

        particle.style.left = x + "px";
        particle.style.top = y + "px";

        particle.style.setProperty(
            "--x",
            ((Math.random() - 0.5) * 500) + "px"
        );

        particle.style.setProperty(
            "--y",
            ((Math.random() - 0.5) * 500) + "px"
        );

        particle.style.background =
            ["#f6a4c7",
             "#ffd1e5",
             "#ffffff",
             "#e9b0df",
             "#f3c0dc"]
            [Math.floor(Math.random() * 5)];

        document.body.appendChild(particle);

        setTimeout(function() {

            particle.remove();

        }, 1300);
    }
}


/* =====================================================
   CAKE CONFETTI
===================================================== */

function cakeConfetti() {

    const box =
        document.getElementById("confettiBox");

    const pieces = 45;

    for (let i = 0; i < pieces; i++) {

        const piece =
            document.createElement("div");

        piece.className = "confetti";

        piece.style.left =
            Math.random() * 100 + "%";

        piece.style.background =
            ["#f7a7c9",
             "#ffd166",
             "#b7d7f0",
             "#d9a7e9",
             "#ffffff",
             "#f4c2d7"]
            [Math.floor(Math.random() * 6)];

        piece.style.animationDelay =
            Math.random() * 0.8 + "s";

        piece.style.transform =
            "rotate(" +
            Math.random() * 360 +
            "deg)";

        box.appendChild(piece);

        setTimeout(function() {
            piece.remove();
        }, 3000);
    }
}


/* Cake confetti after candle */

setTimeout(function() {

    const observer =
        new MutationObserver(function() {

            const cake =
                document.getElementById("page3");

            if (
                cake &&
                cake.classList.contains("active")
            ) {

                cakeConfetti();

                observer.disconnect();
            }

        });

    observer.observe(
        document.body,
        {
            attributes: true,
            subtree: true,
            attributeFilter: ["class"]
        }
    );

}, 100);


/* =====================================================
   BALLOON POP
===================================================== */

function popBalloon(balloon, message) {

    if (balloon.classList.contains("popped")) {
        return;
    }

    balloon.classList.add("popped");

    const rect =
        balloon.getBoundingClientRect();

    createParticles(
        rect.left + rect.width / 2,
        rect.top + rect.height / 2,
        18
    );

    const messageBox =
        document.getElementById("balloonMessage");

    messageBox.innerText = message;

    messageBox.classList.remove("show");

    void messageBox.offsetWidth;

    messageBox.classList.add("show");
}


/* =====================================================
   ENVELOPE
===================================================== */

function openEnvelope() {

    const envelope =
        document.getElementById("envelope");

    envelope.classList.toggle("open");

}


/* =====================================================
   FINAL POP
===================================================== */

function finalPop() {

    createParticles(
        window.innerWidth / 2,
        window.innerHeight / 2,
        70
    );

    cakeConfetti();

    const heart =
        document.querySelector(".final-heart");

    heart.style.animation =
        "heartBlast 0.7s forwards";

}

</script>

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
# RUN
# ---------------------------------------------------------

components.html(
    html,
    height=850,
    scrolling=False
)
