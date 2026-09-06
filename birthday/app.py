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
# ASSETS
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

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Delius&display=swap" rel="stylesheet">

<style>

/* =========================================================
   BASIC
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
========================================================= */

.app {
    position: relative;

    width: 100%;
    height: 100vh;
    min-height: 700px;

    overflow: hidden;

    background:
        radial-gradient(
            circle at 50% 40%,
            rgba(178, 74, 155, 0.55),
            transparent 42%
        ),
        linear-gradient(
            180deg,
            #6b2865 0%,
            #46163f 55%,
            #2c0d2b 100%
        );

    color: white;
}


/* =========================================================
   STARS
========================================================= */

.star {
    position: absolute;

    width: 4px;
    height: 4px;

    background: white;

    border-radius: 50%;

    opacity: 0.8;

    box-shadow:
        0 0 7px white;
}

.s1 { top: 10%; left: 19%; }
.s2 { top: 17%; left: 78%; }
.s3 { top: 31%; left: 11%; }
.s4 { top: 39%; right: 9%; }
.s5 { top: 56%; left: 17%; }
.s6 { top: 70%; right: 16%; }
.s7 { top: 83%; left: 34%; }
.s8 { top: 77%; right: 43%; }
.s9 { top: 23%; left: 49%; }
.s10 { top: 63%; right: 31%; }


/* =========================================================
   PAGES
========================================================= */

.page {
    position: absolute;

    inset: 0;

    display: none;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    text-align: center;

    padding: 25px;
}

.page.active {
    display: flex;
}


/* =========================================================
   TEXT
========================================================= */

.small-title {
    font-size: 21px;

    letter-spacing: 1px;

    color: #fff4fa;

    margin-bottom: 18px;
}

.big-title {
    font-family: "Delius", cursive;

    font-size: 42px;

    line-height: 1.15;

    color: white;

    text-shadow:
        0 3px 10px rgba(0,0,0,0.25);
}

.sub-title {
    font-size: 22px;

    color: #ffe4f1;

    margin-top: 8px;
}


/* =========================================================
   BUTTON
========================================================= */

.next-btn {
    margin-top: 22px;

    border: none;
    outline: none;

    padding: 9px 27px;

    border-radius: 30px;

    background:
        linear-gradient(
            180deg,
            #f5afd0,
            #dc7eaf
        );

    color: white;

    font-family: "Patrick Hand", cursive;

    font-size: 19px;

    cursor: pointer;

    box-shadow:
        0 6px 18px rgba(0,0,0,0.25);

    transition: 0.25s;
}

.next-btn:hover {
    transform: scale(1.06);
}


/* =========================================================
   PAGE 1 - HEART + ARROW
========================================================= */

.first-heart-area {
    position: relative;

    width: 270px;
    height: 255px;
}


/* Heart */

.start-heart {
    position: absolute;

    width: 95px;
    height: 95px;

    left: 88px;
    top: 76px;

    background: #f08ab4;

    transform: rotate(-45deg);

    border-radius: 12px;

    cursor: pointer;

    box-shadow:
        0 0 28px rgba(255,139,190,0.5);

    z-index: 3;

    transition: 0.2s;
}

.start-heart:before,
.start-heart:after {
    content: "";

    position: absolute;

    width: 95px;
    height: 95px;

    background: #f08ab4;

    border-radius: 50%;
}

.start-heart:before {
    top: -47px;
    left: 0;
}

.start-heart:after {
    top: 0;
    left: 47px;
}


/* Arrow */

.arrow {
    position: absolute;

    width: 125px;
    height: 6px;

    left: 112px;
    top: 108px;

    background: #67233d;

    border-radius: 10px;

    transform: rotate(-40deg);

    transform-origin: left center;

    z-index: 8;

    animation: arrowMove 1.4s infinite alternate;
}

.arrow:after {
    content: "";

    position: absolute;

    right: -2px;
    top: -7px;

    border-left: 18px solid #67233d;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
}

@keyframes arrowMove {

    from {
        transform:
            rotate(-40deg)
            translateX(0);
    }

    to {
        transform:
            rotate(-40deg)
            translateX(8px);
    }
}


/* Heart blast */

.blast-heart {
    animation:
        heartBlast 0.65s forwards;
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


/* Pink spread */

.pink-flash {
    position: fixed;

    inset: 0;

    background: #ef94bd;

    opacity: 0;

    pointer-events: none;

    z-index: 1000;
}

.pink-flash.show {
    animation:
        pinkSpread 1.1s forwards;
}

@keyframes pinkSpread {

    0% {
        opacity: 0;
    }

    20% {
        opacity: 0.95;
    }

    100% {
        opacity: 0;
    }
}


/* =========================================================
   CONFETTI / PAPER PIECES
========================================================= */

.particle {
    position: fixed;

    width: 7px;
    height: 10px;

    pointer-events: none;

    z-index: 2000;

    animation:
        particleFly 1.4s ease-out forwards;
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
            rotate(720deg)
            scale(0.4);

        opacity: 0;
    }
}


/* =========================================================
   PAGE 2 - NEW TREE
========================================================= */

.tree-wrapper {

    position: relative;

    width: 390px;
    height: 420px;

    display: flex;

    align-items: center;

    justify-content: center;

    margin-top: -12px;

}


/* ---------------------------------------------------------
   TREE BODY
--------------------------------------------------------- */

.love-tree {

    position: relative;

    width: 350px;
    height: 410px;

}


/* ---------------------------------------------------------
   GROUND
--------------------------------------------------------- */

.tree-ground {

    position: absolute;

    left: 50%;

    bottom: 12px;

    width: 190px;
    height: 17px;

    transform:
        translateX(-50%)
        scaleX(0);

    border-radius: 50%;

    background: rgba(35, 8, 30, 0.45);

    animation:
        groundGrow
        0.7s
        0.2s
        ease-out
        forwards;

}

@keyframes groundGrow {

    to {
        transform:
            translateX(-50%)
            scaleX(1);
    }

}


/* ---------------------------------------------------------
   MAIN TRUNK
--------------------------------------------------------- */

.tree-trunk {

    position: absolute;

    left: 50%;

    bottom: 25px;

    width: 25px;

    height: 245px;

    transform:
        translateX(-50%)
        scaleY(0);

    transform-origin: bottom center;

    border-radius: 18px 18px 10px 10px;

    background:
        linear-gradient(
            90deg,
            #48162b 0%,
            #742d43 35%,
            #8c4053 52%,
            #5c2038 75%,
            #391126 100%
        );

    box-shadow:
        3px 5px 12px rgba(0,0,0,0.3);

    animation:
        trunkGrow
        1.7s
        0.3s
        cubic-bezier(.2,.8,.3,1)
        forwards;

}


@keyframes trunkGrow {

    0% {
        transform:
            translateX(-50%)
            scaleY(0);
    }

    80% {
        transform:
            translateX(-50%)
            scaleY(1.04);
    }

    100% {
        transform:
            translateX(-50%)
            scaleY(1);
    }

}


/* ---------------------------------------------------------
   BRANCHES
--------------------------------------------------------- */

.branch {

    position: absolute;

    height: 13px;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            #3c1228,
            #6d2941,
            #46152e
        );

    transform-origin: left center;

    transform:
        scaleX(0);

    opacity: 0;

}


/* left lower branch */

.branch-1 {

    width: 115px;

    left: 50%;

    bottom: 125px;

    transform:
        rotate(-38deg)
        scaleX(0);

    animation:
        branchLeft
        0.85s
        1.45s
        ease-out
        forwards;

}


/* right lower branch */

.branch-2 {

    width: 112px;

    left: 50%;

    bottom: 145px;

    transform:
        rotate(-325deg)
        scaleX(0);

    animation:
        branchRight
        0.85s
        1.65s
        ease-out
        forwards;

}


/* left upper */

.branch-3 {

    width: 100px;

    left: 50%;

    bottom: 185px;

    transform:
        rotate(-145deg)
        scaleX(0);

    animation:
        branchLeftUp
        0.75s
        1.85s
        ease-out
        forwards;

}


/* right upper */

.branch-4 {

    width: 105px;

    left: 50%;

    bottom: 205px;

    transform:
        rotate(-35deg)
        scaleX(0);

    animation:
        branchRightUp
        0.75s
        2.0s
        ease-out
        forwards;

}


/* top branch */

.branch-5 {

    width: 82px;

    left: 50%;

    bottom: 245px;

    transform:
        rotate(-140deg)
        scaleX(0);

    animation:
        branchTop
        0.7s
        2.15s
        ease-out
        forwards;

}


@keyframes branchLeft {

    0% {
        opacity: 0;
        transform:
            rotate(-38deg)
            scaleX(0);
    }

    100% {
        opacity: 1;
        transform:
            rotate(-38deg)
            scaleX(1);
    }

}

@keyframes branchRight {

    0% {
        opacity: 0;
        transform:
            rotate(-325deg)
            scaleX(0);
    }

    100% {
        opacity: 1;
        transform:
            rotate(-325deg)
            scaleX(1);
    }

}

@keyframes branchLeftUp {

    0% {
        opacity: 0;
        transform:
            rotate(-145deg)
            scaleX(0);
    }

    100% {
        opacity: 1;
        transform:
            rotate(-145deg)
            scaleX(1);
    }

}

@keyframes branchRightUp {

    0% {
        opacity: 0;
        transform:
            rotate(-35deg)
            scaleX(0);
    }

    100% {
        opacity: 1;
        transform:
            rotate(-35deg)
            scaleX(1);
    }

}

@keyframes branchTop {

    0% {
        opacity: 0;
        transform:
            rotate(-140deg)
            scaleX(0);
    }

    100% {
        opacity: 1;
        transform:
            rotate(-140deg)
            scaleX(1);
    }

}


/* ---------------------------------------------------------
   HEART LEAVES
--------------------------------------------------------- */

.heart-leaf {

    position: absolute;

    color: #f39ac1;

    font-family: Arial, sans-serif;

    line-height: 1;

    opacity: 0;

    transform:
        translateY(15px)
        scale(0);

    text-shadow:
        0 2px 8px rgba(255,150,200,0.35);

    animation:
        heartLeafGrow
        0.65s
        ease-out
        forwards;

}


/* different pink shades */

.h1,
.h4,
.h8,
.h13,
.h18,
.h23 {

    color: #f7afd0;

}

.h2,
.h6,
.h10,
.h15,
.h20,
.h25 {

    color: #ed8fba;

}

.h3,
.h7,
.h12,
.h17,
.h22,
.h27 {

    color: #f6a2c7;

}


/* heart positions */

.h1 {
    left: 43px;
    top: 145px;
    font-size: 31px;
    animation-delay: 2.05s;
}

.h2 {
    left: 70px;
    top: 118px;
    font-size: 24px;
    animation-delay: 2.18s;
}

.h3 {
    left: 92px;
    top: 92px;
    font-size: 29px;
    animation-delay: 2.31s;
}

.h4 {
    left: 128px;
    top: 65px;
    font-size: 25px;
    animation-delay: 2.44s;
}

.h5 {
    left: 161px;
    top: 78px;
    font-size: 34px;
    animation-delay: 2.57s;
}

.h6 {
    left: 195px;
    top: 63px;
    font-size: 24px;
    animation-delay: 2.70s;
}

.h7 {
    left: 225px;
    top: 91px;
    font-size: 30px;
    animation-delay: 2.83s;
}

.h8 {
    left: 251px;
    top: 118px;
    font-size: 25px;
    animation-delay: 2.96s;
}

.h9 {
    left: 273px;
    top: 148px;
    font-size: 31px;
    animation-delay: 3.09s;
}

.h10 {
    left: 66px;
    top: 158px;
    font-size: 25px;
    animation-delay: 3.22s;
}

.h11 {
    left: 95px;
    top: 137px;
    font-size: 22px;
    animation-delay: 3.35s;
}

.h12 {
    left: 122px;
    top: 119px;
    font-size: 31px;
    animation-delay: 3.48s;
}

.h13 {
    left: 151px;
    top: 106px;
    font-size: 23px;
    animation-delay: 3.61s;
}

.h14 {
    left: 180px;
    top: 111px;
    font-size: 29px;
    animation-delay: 3.74s;
}

.h15 {
    left: 207px;
    top: 126px;
    font-size: 22px;
    animation-delay: 3.87s;
}

.h16 {
    left: 234px;
    top: 143px;
    font-size: 29px;
    animation-delay: 4.00s;
}

.h17 {
    left: 82px;
    top: 184px;
    font-size: 28px;
    animation-delay: 4.13s;
}

.h18 {
    left: 111px;
    top: 169px;
    font-size: 23px;
    animation-delay: 4.26s;
}

.h19 {
    left: 139px;
    top: 153px;
    font-size: 30px;
    animation-delay: 4.39s;
}

.h20 {
    left: 168px;
    top: 145px;
    font-size: 23px;
    animation-delay: 4.52s;
}

.h21 {
    left: 196px;
    top: 155px;
    font-size: 31px;
    animation-delay: 4.65s;
}

.h22 {
    left: 223px;
    top: 170px;
    font-size: 23px;
    animation-delay: 4.78s;
}

.h23 {
    left: 250px;
    top: 185px;
    font-size: 28px;
    animation-delay: 4.91s;
}

.h24 {
    left: 106px;
    top: 205px;
    font-size: 25px;
    animation-delay: 5.04s;
}

.h25 {
    left: 134px;
    top: 194px;
    font-size: 22px;
    animation-delay: 5.17s;
}

.h26 {
    left: 164px;
    top: 190px;
    font-size: 29px;
    animation-delay: 5.30s;
}

.h27 {
    left: 194px;
    top: 198px;
    font-size: 24px;
    animation-delay: 5.43s;
}

.h28 {
    left: 220px;
    top: 208px;
    font-size: 28px;
    animation-delay: 5.56s;
}


/* heart animation */

@keyframes heartLeafGrow {

    0% {
        opacity: 0;

        transform:
            translateY(18px)
            scale(0)
            rotate(-20deg);
    }

    55% {
        opacity: 1;

        transform:
            translateY(-3px)
            scale(1.18)
            rotate(7deg);
    }

    100% {
        opacity: 1;

        transform:
            translateY(0)
            scale(1)
            rotate(0deg);
    }

}


/* gentle floating after appearing */

.heart-leaf {

    animation-name:
        heartLeafGrow,
        tinyHeartFloat;

    animation-duration:
        0.65s,
        2.7s;

    animation-timing-function:
        ease-out,
        ease-in-out;

    animation-iteration-count:
        1,
        infinite;

    animation-fill-mode:
        forwards,
        both;

}


/* ---------------------------------------------------------
   LITTLE HEART HIGHLIGHTS
--------------------------------------------------------- */

.tree-spark {

    position: absolute;

    color: #fff2f8;

    font-family: Arial, sans-serif;

    opacity: 0;

    animation:
        sparkAppear
        0.5s
        5.3s
        forwards;

}

.spark1 {
    left: 51px;
    top: 102px;
    font-size: 10px;
}

.spark2 {
    right: 53px;
    top: 125px;
    font-size: 8px;
}

.spark3 {
    left: 91px;
    top: 74px;
    font-size: 7px;
}

.spark4 {
    right: 88px;
    top: 85px;
    font-size: 10px;
}


@keyframes sparkAppear {

    to {
        opacity: 0.8;
    }

}


/* ---------------------------------------------------------
   FLOATING MOTION
--------------------------------------------------------- */

@keyframes tinyHeartFloat {

    0% {
        margin-top: 0;
    }

    50% {
        margin-top: -3px;
    }

    100% {
        margin-top: 0;
    }

}


/* =========================================================
   PAGE 3 - CAKE
========================================================= */

.cake-area {
    position: relative;

    width: 350px;
    height: 430px;

    margin-top: -12px;
}


/* Plate */

.plate {
    position: absolute;

    width: 260px;
    height: 22px;

    left: 45px;
    bottom: 35px;

    border-radius: 50%;

    background: #fff8fc;

    box-shadow:
        0 7px 14px rgba(0,0,0,0.2);
}


/* Cake layers */

.cake-layer {
    position: absolute;

    left: 50%;

    transform:
        translateX(-50%)
        translateY(-330px);

    opacity: 0;

    border-radius: 9px;

    background:
        linear-gradient(
            180deg,
            #f7b4d1,
            #db79aa
        );

    box-shadow:
        0 8px 14px rgba(0,0,0,0.25);
}


/* Bottom */

.layer3 {
    width: 245px;
    height: 68px;

    bottom: 52px;
}


/* Middle */

.layer2 {
    width: 210px;
    height: 62px;

    bottom: 110px;
}


/* Top */

.layer1 {
    width: 165px;
    height: 55px;

    bottom: 162px;
}


/* Layer falling */

.cake-area.build .layer3 {
    animation:
        cakeFall 0.75s 0.2s ease-out forwards;
}

.cake-area.build .layer2 {
    animation:
        cakeFall 0.75s 1.0s ease-out forwards;
}

.cake-area.build .layer1 {
    animation:
        cakeFall 0.75s 1.8s ease-out forwards;
}

@keyframes cakeFall {

    0% {
        opacity: 0;

        transform:
            translateX(-50%)
            translateY(-330px)
            rotate(-5deg);
    }

    70% {
        opacity: 1;

        transform:
            translateX(-50%)
            translateY(10px)
            rotate(2deg);
    }

    100% {
        opacity: 1;

        transform:
            translateX(-50%)
            translateY(0)
            rotate(0deg);
    }
}


/* Cream */

.cream {
    position: absolute;

    left: 50%;

    transform:
        translateX(-50%)
        translateY(-280px);

    opacity: 0;

    height: 15px;

    border-radius: 50%;

    background: #fffaff;

    z-index: 5;
}

.cream1 {
    width: 150px;
    bottom: 155px;
}

.cream2 {
    width: 198px;
    bottom: 105px;
}

.cream3 {
    width: 232px;
    bottom: 47px;
}


.cake-area.build .cream1 {
    animation:
        creamFall 0.55s 2.45s forwards;
}

.cake-area.build .cream2 {
    animation:
        creamFall 0.55s 2.7s forwards;
}

.cake-area.build .cream3 {
    animation:
        creamFall 0.55s 2.95s forwards;
}

@keyframes creamFall {

    0% {
        opacity: 0;

        transform:
            translateX(-50%)
            translateY(-280px)
            scaleX(0.7);
    }

    70% {
        transform:
            translateX(-50%)
            translateY(7px)
            scaleX(1.05);
    }

    100% {
        opacity: 1;

        transform:
            translateX(-50%)
            translateY(0)
            scaleX(1);
    }
}


/* Candle */

.candle {
    position: absolute;

    width: 19px;
    height: 75px;

    left: 50%;

    bottom: 215px;

    transform:
        translateX(-50%)
        translateY(-220px);

    opacity: 0;

    z-index: 8;

    border-radius: 5px;

    background:
        repeating-linear-gradient(
            -45deg,
            #ffffff 0px,
            #ffffff 8px,
            #efa2c5 8px,
            #efa2c5 16px
        );
}


.cake-area.build .candle {
    animation:
        candleFall 0.7s 3.35s ease-out forwards;
}

@keyframes candleFall {

    0% {
        opacity: 0;

        transform:
            translateX(-50%)
            translateY(-220px)
            rotate(-10deg);
    }

    75% {
        transform:
            translateX(-50%)
            translateY(8px)
            rotate(3deg);
    }

    100% {
        opacity: 1;

        transform:
            translateX(-50%)
            translateY(0)
            rotate(0deg);
    }
}


/* Flame */

.flame {
    position: absolute;

    width: 20px;
    height: 28px;

    left: 50%;

    bottom: 282px;

    transform:
        translateX(-50%)
        translateY(-150px)
        rotate(45deg);

    opacity: 0;

    z-index: 9;

    background: #ffe59a;

    border-radius:
        50% 50% 50% 0;

    box-shadow:
        0 0 18px #ffd66d;
}


.cake-area.build .flame {
    animation:
        flameFall 0.55s 4.0s forwards,
        flicker 0.8s 4.55s infinite alternate;
}

@keyframes flameFall {

    from {
        opacity: 0;

        transform:
            translateX(-50%)
            translateY(-150px)
            rotate(45deg);
    }

    to {
        opacity: 1;

        transform:
            translateX(-50%)
            translateY(0)
            rotate(45deg);
    }
}

@keyframes flicker {

    from {
        transform:
            translateX(-50%)
            rotate(40deg)
            scale(0.9);
    }

    to {
        transform:
            translateX(-50%)
            rotate(50deg)
            scale(1.08);
    }
}


/* Cake message */

.cake-message {
    position: absolute;

    left: 50%;

    bottom: -4px;

    width: 100%;

    transform:
        translateX(-50%)
        translateY(20px);

    opacity: 0;

    font-family: "Delius", cursive;

    font-size: 36px;

    line-height: 1.12;
}

.cake-message.show {
    animation:
        cakeMessageShow 0.8s 4.45s forwards;
}

@keyframes cakeMessageShow {

    to {
        opacity: 1;

        transform:
            translateX(-50%)
            translateY(0);
    }
}


/* =========================================================
   PAGE 4 - BALLOONS
========================================================= */

.balloon-title {
    font-size: 25px;

    margin-bottom: 22px;
}

.balloon-area {
    position: relative;

    width: 370px;
    height: 350px;
}


/* Balloon */

.balloon {
    position: absolute;

    width: 78px;
    height: 100px;

    border-radius:
        50% 50% 46% 46%;

    cursor: pointer;

    box-shadow:
        inset -12px -10px 18px rgba(0,0,0,0.13),
        inset 8px 5px 12px rgba(255,255,255,0.3);

    transition: 0.15s;
}

.balloon:after {
    content: "";

    position: absolute;

    width: 2px;
    height: 105px;

    left: 50%;
    top: 97px;

    background: rgba(255,255,255,0.6);
}

.balloon:before {
    content: "";

    position: absolute;

    bottom: -7px;
    left: 50%;

    transform:
        translateX(-50%);

    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 10px solid currentColor;
}


.b1 {
    left: 40px;
    top: 55px;

    background: #f3a2c5;
    color: #f3a2c5;
}

.b2 {
    left: 145px;
    top: 10px;

    background: #e4afd9;
    color: #e4afd9;
}

.b3 {
    left: 250px;
    top: 55px;

    background: #a8c4dd;
    color: #a8c4dd;
}

.b4 {
    left: 145px;
    top: 145px;

    background: #f2bad7;
    color: #f2bad7;
}


.balloon:hover {
    transform:
        translateY(-6px)
        scale(1.05);
}


/* POP */

.balloon.popped {
    animation:
        balloonPop 0.35s forwards;
}

@keyframes balloonPop {

    0% {
        transform: scale(1);
        opacity: 1;
    }

    40% {
        transform: scale(1.25);
        opacity: 0.9;
    }

    100% {
        transform: scale(0);
        opacity: 0;
    }
}


/* Balloon message */

.balloon-message {
    position: absolute;

    left: 50%;
    bottom: 5px;

    width: 320px;

    transform:
        translateX(-50%)
        translateY(20px);

    opacity: 0;

    font-size: 21px;

    color: #fff5fb;

    transition: 0.4s;
}

.balloon-message.show {
    opacity: 1;

    transform:
        translateX(-50%)
        translateY(0);
}


/* =========================================================
   PAGE 5 - PHOTOS
========================================================= */

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
        9px
        9px
        15px;

    background: white;

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

    font-size: 19px;

    line-height: 1.1;

    margin-top: 10px;
}


/* =========================================================
   PAGE 6 - ENVELOPE
========================================================= */

.envelope-page {
    justify-content: center;
}


/* Wrapper stays CENTER */

.envelope-wrap {
    position: relative;

    width: 360px;
    height: 280px;

    display: flex;

    align-items: center;
    justify-content: center;

    opacity: 0;
}

.envelope-wrap.enter {
    animation:
        envelopeAppear 1s ease-out forwards;
}

@keyframes envelopeAppear {

    from {
        opacity: 0;

        transform:
            scale(0.75)
            translateY(30px);
    }

    to {
        opacity: 1;

        transform:
            scale(1)
            translateY(0);
    }
}


/* Envelope */

.envelope {
    position: relative;

    width: 300px;
    height: 190px;

    background: #f4afd0;

    border-radius: 8px;

    box-shadow:
        0 12px 28px rgba(0,0,0,0.28);

    cursor: pointer;
}


/* Top flap */

.envelope:before {
    content: "";

    position: absolute;

    left: 0;
    top: 0;

    width: 0;
    height: 0;

    border-left: 150px solid transparent;
    border-right: 150px solid transparent;
    border-top: 105px solid #e38bb6;

    transform-origin: top center;

    transition: 0.7s;

    z-index: 6;
}


/* Bottom fold */

.envelope:after {
    content: "";

    position: absolute;

    left: 0;
    bottom: 0;

    width: 0;
    height: 0;

    border-left: 150px solid #ef9fc3;
    border-top: 95px solid transparent;

    z-index: 5;
}


/* Letter */

.envelope-letter {
    position: absolute;

    left: 22px;
    right: 22px;

    bottom: 8px;

    height: 155px;

    padding:
        18px
        17px;

    background: #fff7ed;

    color: #4b2943;

    border-radius: 5px;

    font-size: 17px;

    line-height: 1.18;

    text-align: left;

    overflow: auto;

    transition: 0.7s;

    z-index: 2;
}


.envelope.open:before {
    transform:
        rotateX(180deg);
}

.envelope.open .envelope-letter {
    transform:
        translateY(-120px);

    height: 245px;

    z-index: 10;
}


.letter-title {
    text-align: center;

    font-family: "Delius", cursive;

    font-size: 24px;

    color: #7b315c;

    margin-bottom: 10px;
}


.from {
    text-align: right;

    font-size: 21px;

    color: #8d3265;

    margin-top: 12px;
}


/* =========================================================
   PAGE 7 - FINAL
========================================================= */

.final-heart {
    position: relative;

    width: 115px;
    height: 115px;

    background: #e74468;

    transform:
        rotate(-45deg);

    border-radius: 15px;

    margin-bottom: 42px;

    animation:
        heartBeat 1.2s infinite;
}

.final-heart:before,
.final-heart:after {
    content: "";

    position: absolute;

    width: 115px;
    height: 115px;

    background: #e74468;

    border-radius: 50%;
}

.final-heart:before {
    top: -57px;
    left: 0;
}

.final-heart:after {
    top: 0;
    left: 57px;
}


@keyframes heartBeat {

    0%, 100% {
        transform:
            rotate(-45deg)
            scale(1);
    }

    50% {
        transform:
            rotate(-45deg)
            scale(1.09);
    }
}


.final-title {
    font-family: "Delius", cursive;

    font-size: 47px;

    line-height: 1.1;
}

.final-name {
    font-family: "Delius", cursive;

    font-size: 39px;

    color: #f7b1cf;

    margin-top: 6px;
}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 600px) {

    .big-title {
        font-size: 34px;
    }

    .tree-wrapper {
        transform: scale(0.82);

        margin-top: -35px;
        margin-bottom: -35px;
    }

    .cake-area {
        transform: scale(0.82);

        margin-top: -45px;
        margin-bottom: -35px;
    }

    .photo-container {
        gap: 7px;
    }

    .photo-card {
        width: 31%;

        padding: 5px;
    }

    .photo-card img {
        height: 170px;
    }

    .photo-caption {
        font-size: 13px;
    }

    .envelope-wrap {
        transform: scale(0.86);
    }

    .envelope-wrap.enter {
        animation:
            envelopeAppearMobile 1s ease-out forwards;
    }

    @keyframes envelopeAppearMobile {

        from {
            opacity: 0;
            transform:
                scale(0.7)
                translateY(30px);
        }

        to {
            opacity: 1;
            transform:
                scale(0.86)
                translateY(0);
        }
    }

    .final-title {
        font-size: 38px;
    }

    .final-name {
        font-size: 32px;
    }

}

</style>

</head>


<body>

<div class="app">

    <!-- STARS -->

    <div class="star s1"></div>
    <div class="star s2"></div>
    <div class="star s3"></div>
    <div class="star s4"></div>
    <div class="star s5"></div>
    <div class="star s6"></div>
    <div class="star s7"></div>
    <div class="star s8"></div>
    <div class="star s9"></div>
    <div class="star s10"></div>


    <div
        class="pink-flash"
        id="pinkFlash">
    </div>


    <!-- =====================================================
         PAGE 1
    ====================================================== -->

    <section
        class="page active"
        id="page1">

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


    <!-- =====================================================
         PAGE 2 - TREE
    ====================================================== -->

    <section
        class="page"
        id="page2">

        <div class="small-title">
            First things first
        </div>


        <div class="tree-wrapper">

            <div class="love-tree">


                <!-- GROUND -->

                <div class="tree-ground"></div>


                <!-- MAIN TRUNK -->

                <div class="tree-trunk"></div>


                <!-- BRANCHES -->

                <div class="branch branch-1"></div>

                <div class="branch branch-2"></div>

                <div class="branch branch-3"></div>

                <div class="branch branch-4"></div>

                <div class="branch branch-5"></div>


                <!-- MANY HEART LEAVES -->

                <span class="heart-leaf h1">♥</span>
                <span class="heart-leaf h2">♥</span>
                <span class="heart-leaf h3">♥</span>
                <span class="heart-leaf h4">♥</span>
                <span class="heart-leaf h5">♥</span>
                <span class="heart-leaf h6">♥</span>
                <span class="heart-leaf h7">♥</span>
                <span class="heart-leaf h8">♥</span>
                <span class="heart-leaf h9">♥</span>
                <span class="heart-leaf h10">♥</span>
                <span class="heart-leaf h11">♥</span>
                <span class="heart-leaf h12">♥</span>
                <span class="heart-leaf h13">♥</span>
                <span class="heart-leaf h14">♥</span>
                <span class="heart-leaf h15">♥</span>
                <span class="heart-leaf h16">♥</span>
                <span class="heart-leaf h17">♥</span>
                <span class="heart-leaf h18">♥</span>
                <span class="heart-leaf h19">♥</span>
                <span class="heart-leaf h20">♥</span>
                <span class="heart-leaf h21">♥</span>
                <span class="heart-leaf h22">♥</span>
                <span class="heart-leaf h23">♥</span>
                <span class="heart-leaf h24">♥</span>
                <span class="heart-leaf h25">♥</span>
                <span class="heart-leaf h26">♥</span>
                <span class="heart-leaf h27">♥</span>
                <span class="heart-leaf h28">♥</span>


                <!-- SMALL SPARKLES -->

                <span class="tree-spark spark1">♥</span>
                <span class="tree-spark spark2">♥</span>
                <span class="tree-spark spark3">♥</span>
                <span class="tree-spark spark4">♥</span>

            </div>

        </div>


        <div class="big-title">
            A little tree<br>
            full of love
        </div>


        <button
            class="next-btn"
            onclick="showPage(3)">
            Next
        </button>

    </section>


    <!-- =====================================================
         PAGE 3 - CAKE
    ====================================================== -->

    <section
        class="page"
        id="page3">

        <div class="small-title">
            Something special is coming...
        </div>


        <div
            class="cake-area"
            id="cakeArea">


            <div class="plate"></div>


            <div
                class="cake-layer layer3">
            </div>


            <div
                class="cake-layer layer2">
            </div>


            <div
                class="cake-layer layer1">
            </div>


            <div
                class="cream cream1">
            </div>

            <div
                class="cream cream2">
            </div>

            <div
                class="cream cream3">
            </div>


            <div
                class="candle">
            </div>


            <div
                class="flame">
            </div>


            <div
                class="cake-message"
                id="cakeMessage">

                HAPPY BIRTHDAY<br>
                RICKY

            </div>

        </div>


        <button
            class="next-btn"
            onclick="showPage(4)">

            Continue

        </button>

    </section>


    <!-- =====================================================
         PAGE 4 - BALLOONS
    ====================================================== -->

    <section
        class="page"
        id="page4">

        <div class="balloon-title">
            Pop the balloons
        </div>


        <div class="balloon-area">


            <div
                class="balloon b1"
                onclick="popBalloon(this,1)">
            </div>


            <div
                class="balloon b2"
                onclick="popBalloon(this,2)">
            </div>


            <div
                class="balloon b3"
                onclick="popBalloon(this,3)">
            </div>


            <div
                class="balloon b4"
                onclick="popBalloon(this,4)">
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
            style="
                opacity:0;
                pointer-events:none;
            ">

            Continue

        </button>

    </section>


    <!-- =====================================================
         PAGE 5 - PHOTOS
    ====================================================== -->

    <section
        class="page"
        id="page5">

        <div class="memory-title">
            A walk down memory lane
        </div>


        <div class="photo-container">


            <div class="photo-card">

                <img
                    src="data:image/jpeg;base64,__PHOTO1__"
                >

                <div class="photo-caption">
                    One of my favourite pictures of you
                </div>

            </div>


            <div class="photo-card">

                <img
                    src="data:image/jpeg;base64,__PHOTO2__"
                >

                <div class="photo-caption">
                    A moment I really love
                </div>

            </div>


            <div class="photo-card">

                <img
                    src="data:image/jpeg;base64,__PHOTO3__"
                >

                <div class="photo-caption">
                    A picture that always makes me smile
                </div>

            </div>

        </div>


        <button
            class="next-btn"
            onclick="showPage(6)">

            Next

        </button>

    </section>


    <!-- =====================================================
         PAGE 6 - ENVELOPE
    ====================================================== -->

    <section
        class="page envelope-page"
        id="page6">


        <div class="small-title">
            One little letter for you
        </div>


        <div
            class="envelope-wrap"
            id="envelopeWrap">


            <div
                class="envelope"
                id="envelope"
                onclick="openEnvelope()">


                <div class="envelope-letter">


                    <div class="letter-title">
                        For you
                    </div>


                    <div>
                        You are someone who has become very
                        special to my heart.
                    </div>


                    <br>


                    <div>
                        When I think about the future, I hope
                        it is filled with two people who understand
                        each other, support each other and never
                        stop choosing each other.
                    </div>


                    <br>


                    <div>
                        If life gives us the chance to walk
                        through that beautiful journey together,
                        I would love to create a life filled with
                        peace, laughter, little adventures and
                        countless memories with you.
                    </div>


                    <br>


                    <div>
                        I don't need everything to be perfect.
                        I just want something real, where we
                        grow together and stand beside each
                        other through every chapter.
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
            style="
                opacity:0;
                pointer-events:none;
            ">

            Next

        </button>

    </section>


    <!-- =====================================================
         PAGE 7 - FINAL
    ====================================================== -->

    <section
        class="page"
        id="page7">


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

/* =========================================================
   PAGE CONTROL
========================================================= */

function showPage(number) {

    document
        .querySelectorAll(".page")
        .forEach(function(page) {

            page.classList.remove("active");

        });


    const selected =
        document.getElementById("page" + number);


    if (selected) {

        selected.classList.add("active");

    }


    /* TREE */

    if (number === 2) {

        const tree =
            document.querySelector(".love-tree");

        tree.style.display = "none";

        setTimeout(function() {

            tree.style.display = "block";

        }, 20);

    }


    /* CAKE */

    if (number === 3) {

        const cake =
            document.getElementById("cakeArea");

        cake.classList.remove("build");

        void cake.offsetWidth;

        cake.classList.add("build");


        setTimeout(function() {

            document
                .getElementById("cakeMessage")
                .classList.add("show");

        }, 100);


        setTimeout(function() {

            createConfetti(
                window.innerWidth / 2,
                window.innerHeight / 2 - 90,
                42
            );

        }, 4450);

    }


    /* ENVELOPE */

    if (number === 6) {

        const wrap =
            document.getElementById("envelopeWrap");

        wrap.classList.remove("enter");

        void wrap.offsetWidth;

        wrap.classList.add("enter");

    }


    /* FINAL PAGE */

    if (number === 7) {

        setTimeout(function() {

            createConfetti(
                window.innerWidth / 2,
                window.innerHeight / 2,
                85
            );

        }, 450);

    }

}


/* =========================================================
   STARTING HEART
========================================================= */

function startSurprise() {

    const heart =
        document.getElementById("startHeart");


    heart.classList.add("blast-heart");


    createHeartParticles(
        window.innerWidth / 2,
        window.innerHeight / 2,
        30
    );


    setTimeout(function() {

        document
            .getElementById("pinkFlash")
            .classList.add("show");

    }, 150);


    setTimeout(function() {

        showPage(2);

    }, 850);

}


/* =========================================================
   HEART PARTICLES
========================================================= */

function createHeartParticles(x, y, amount) {

    for (let i = 0; i < amount; i++) {

        const p =
            document.createElement("div");


        p.className = "particle";


        p.innerHTML = "♥";


        p.style.width = "auto";
        p.style.height = "auto";


        p.style.fontSize =
            (9 + Math.random() * 12) + "px";


        p.style.color = "#f39ac1";


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

        }, 1500);

    }

}


/* =========================================================
   COLOURFUL PAPER CONFETTI
========================================================= */

function createConfetti(x, y, amount) {

    const colors = [
        "#f5a3c8",
        "#ffd2e5",
        "#b9d7ed",
        "#e7acd8",
        "#ffe6a8",
        "#ffffff",
        "#d9b3e5"
    ];


    for (let i = 0; i < amount; i++) {

        const p =
            document.createElement("div");


        p.className = "particle";


        p.style.width =
            (5 + Math.random() * 6) + "px";


        p.style.height =
            (7 + Math.random() * 7) + "px";


        p.style.background =
            colors[
                Math.floor(
                    Math.random() * colors.length
                )
            ];


        p.style.borderRadius =
            Math.random() > 0.5
                ? "2px"
                : "0";


        p.style.left = x + "px";
        p.style.top = y + "px";


        const angle =
            Math.random() * Math.PI * 2;


        const distance =
            90 + Math.random() * 280;


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

        }, 1500);

    }

}


/* =========================================================
   BALLOONS
========================================================= */

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

    if (
        balloon.classList.contains("popped")
    ) {
        return;
    }


    balloon.classList.add("popped");


    poppedBalloons++;


    const rect =
        balloon.getBoundingClientRect();


    createConfetti(
        rect.left + rect.width / 2,
        rect.top + rect.height / 2,
        28
    );


    const message =
        document.getElementById(
            "balloonMessage"
        );


    message.innerHTML =
        balloonMessages[number];


    message.classList.remove("show");

    void message.offsetWidth;

    message.classList.add("show");


    if (poppedBalloons === 4) {

        setTimeout(function() {

            const next =
                document.getElementById(
                    "balloonNext"
                );


            next.style.opacity = "1";

            next.style.pointerEvents =
                "auto";


        }, 700);

    }

}


/* =========================================================
   ENVELOPE
========================================================= */

let envelopeOpened = false;


function openEnvelope() {

    if (envelopeOpened) {
        return;
    }


    envelopeOpened = true;


    const envelope =
        document.getElementById(
            "envelope"
        );


    envelope.classList.add("open");


    const rect =
        envelope.getBoundingClientRect();


    createConfetti(
        rect.left + rect.width / 2,
        rect.top + 20,
        22
    );


    setTimeout(function() {

        const next =
            document.getElementById(
                "letterNext"
            );


        next.style.opacity = "1";

        next.style.pointerEvents =
            "auto";


    }, 900);

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
# DISPLAY
# =========================================================

components.html(
    html,
    height=850,
    scrolling=False
)
