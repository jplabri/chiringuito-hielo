import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cubitos al Chiringuito",
    page_icon="🧊",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #64c7ff 0%, #ffe7a3 55%, #f2c16b 100%);
}

.block-container {
    padding-top: 0.35rem;
    padding-bottom: 0.35rem;
    max-width: 1060px;
}

h1 {
    text-align: center;
    color: #064f74;
    margin-bottom: 0.15rem;
    text-shadow: 1px 1px 0 #ffffff;
}

@media (max-width: 760px) {
    .block-container {
        padding-left: 0.05rem;
        padding-right: 0.05rem;
        padding-top: 0.05rem;
    }

    h1 {
        font-size: 1.15rem !important;
        line-height: 1.05 !important;
        margin-bottom: 0.05rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.title("🧊 Cubitos al Chiringuito")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#0b6fa4;
        font-size:16px;
        font-weight:bold;
        margin-bottom:10px;">
        Desarrollado por Jesús Platero
    </div>
    """,
    unsafe_allow_html=True
)

components.html("""
<style>
html, body {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}

button {
    -webkit-tap-highlight-color: transparent;
}

#gameWrap {
    width: 100%;
    display: flex;
    justify-content: center;
}

#game {
    display: block;
    outline: none;
    border: 4px solid #075c7d;
    border-radius: 14px;
    background: #8ed8ff;
    box-shadow: 0 8px 24px rgba(0, 77, 105, 0.28);
}

.control-row {
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 8px;
    flex-wrap: wrap;
}

.main-btn {
    font-family: Arial, sans-serif;
    font-weight: bold;
    padding: 8px 16px;
    border-radius: 10px;
    border: 2px solid #075c7d;
    background: #fff8d7;
    color: #075c7d;
    cursor: pointer;
    touch-action: manipulation;
}

.green-btn {
    background: #20ad6b;
    color: white;
}

.level-btn {
    font-family: Arial, sans-serif;
    font-weight: bold;
    padding: 8px 14px;
    border-radius: 999px;
    border: 2px solid #075c7d;
    background: #fff8d7;
    color: #075c7d;
    cursor: pointer;
    touch-action: manipulation;
}

#touchBar {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 9px;
    margin-top: 9px;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}

.touch-btn {
    font-family: Arial, sans-serif;
    font-weight: bold;
    border-radius: 13px;
    border: 3px solid #075c7d;
    background: #fff8d7;
    color: #075c7d;
    cursor: pointer;
    touch-action: none;
    user-select: none;
}

#btnLeft, #btnRight {
    font-size: 30px;
    width: 76px;
    height: 58px;
}

#btnShoot {
    font-size: 18px;
    min-width: 170px;
    height: 58px;
    background: #20ad6b;
    color: white;
}

#helpText {
    text-align: center;
    color: #064f74;
    font-family: Arial, sans-serif;
    font-weight: bold;
    margin-top: 7px;
    margin-bottom: 0;
    font-size: 14px;
}

@media (max-width: 760px) {
    #game {
        border-width: 3px;
        border-radius: 10px;
    }

    .control-row {
        gap: 6px;
        margin-top: 5px;
    }

    .main-btn {
        padding: 7px 11px !important;
        font-size: 13px !important;
    }

    .level-btn {
        padding: 7px 10px !important;
        font-size: 13px !important;
    }

    #touchBar {
        gap: 6px !important;
        margin-top: 6px !important;
    }

    #btnLeft, #btnRight {
        width: 76px !important;
        height: 60px !important;
        font-size: 30px !important;
    }

    #btnShoot {
        min-width: 145px !important;
        height: 60px !important;
        font-size: 17px !important;
    }

    #helpText {
        display: none;
    }
}
</style>

<div id="gameWrap">
    <canvas id="game" tabindex="0"></canvas>
</div>

<div class="control-row">
    <button id="btnMenu" class="main-btn">M / Menú</button>
    <button id="btnStart" class="main-btn green-btn">ENTER / Continuar</button>
</div>

<div id="levelBar" class="control-row">
    <button id="btnNivel1" class="level-btn">Nivel 1</button>
    <button id="btnNivel2" class="level-btn">Nivel 2</button>
    <button id="btnNivel3" class="level-btn">Nivel 3</button>
</div>

<div id="touchBar">
    <div style="display:flex; gap:7px;">
        <button id="btnLeft" class="touch-btn">←</button>
        <button id="btnRight" class="touch-btn">→</button>
    </div>
    <button id="btnShoot" class="touch-btn">🧊 LANZAR</button>
</div>

<p id="helpText">PC: clic dentro del juego. 1, 2 o 3 eligen nivel. ENTER empieza. ESPACIO lanza hielo. Móvil: ← → y LANZAR.</p>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const BASE_W = 1000;
const BASE_H = 560;
canvas.width = BASE_W;
canvas.height = BASE_H;

const W = BASE_W;
const H = BASE_H;
const esMovil = window.matchMedia("(max-width: 760px)").matches || ("ontouchstart" in window);

function ajustarCanvas() {
    const margenW = esMovil ? 0.99 : 0.94;
    const anchoMax = esMovil ? window.innerWidth * margenW : Math.min(window.innerWidth * margenW, 1040);
    const altoMax = esMovil ? window.innerHeight * 0.76 : Math.min(window.innerHeight * 0.72, 650);
    const altoPorAncho = anchoMax * (BASE_H / BASE_W);
    const altoFinal = Math.min(altoPorAncho, altoMax);
    const anchoFinal = altoFinal * (BASE_W / BASE_H);
    canvas.style.width = `${Math.floor(anchoFinal)}px`;
    canvas.style.height = `${Math.floor(altoFinal)}px`;
}
window.addEventListener("resize", ajustarCanvas);
window.addEventListener("orientationchange", () => setTimeout(ajustarCanvas, 150));
ajustarCanvas();

function enfocarCanvas() {
    try { canvas.focus({preventScroll:true}); } catch (err) { canvas.focus(); }
}
canvas.addEventListener("click", enfocarCanvas);
window.addEventListener("load", enfocarCanvas);
setTimeout(enfocarCanvas, 250);

let estado = "menu";
let puntos = 0;
let puntosNivel = 0;
let vidas = 5;
let nivel = 1;
let nivelElegido = 1;
let record = Number(localStorage.getItem("cubitos_chiringuito_record") || 0);
let esNuevoRecord = false;
let teclas = {};
let rafagas = 0;
let doble = false;
let dobleHasta = 0;
let mensajeNivel = "";
let frame = 0;

let jugador = {x: 470, y: 482, w: 58, h: 50, vel: 8};
let cubitos = [];
let vasos = [];
let soles = [];
let limones = [];
let congeladores = [];
let particulas = [];
let salpicaduras = [];

const btnMenu = document.getElementById("btnMenu");
const btnStart = document.getElementById("btnStart");
const btnLeft = document.getElementById("btnLeft");
const btnRight = document.getElementById("btnRight");
const btnShoot = document.getElementById("btnShoot");
const btnNivel1 = document.getElementById("btnNivel1");
const btnNivel2 = document.getElementById("btnNivel2");
const btnNivel3 = document.getElementById("btnNivel3");

function objetivoNivel() {
    // Ahora el objetivo cuenta VASOS COMPLETOS, no impactos sueltos.
    // Cada vaso necesita 3 cubitos, así que estos niveles duran más y avanzan de forma clara.
    if (nivel === 1) return 9;
    if (nivel === 2) return 14;
    return 20;
}

function pintarBotonesNivel() {
    [btnNivel1, btnNivel2, btnNivel3].forEach((b, i) => {
        const activo = nivelElegido === i + 1;
        b.style.background = activo ? "#20ad6b" : "#fff8d7";
        b.style.color = activo ? "white" : "#075c7d";
    });
}

function elegirNivel(n) {
    nivelElegido = n;
    pintarBotonesNivel();
    enfocarCanvas();
}
btnNivel1.addEventListener("click", () => elegirNivel(1));
btnNivel2.addEventListener("click", () => elegirNivel(2));
btnNivel3.addEventListener("click", () => elegirNivel(3));
pintarBotonesNivel();

let audioCtx = null;

function obtenerAudioCtx() {
    try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return null;

        if (!audioCtx) {
            audioCtx = new AudioCtx();
        }

        if (audioCtx.state === "suspended") {
            audioCtx.resume();
        }

        return audioCtx;
    } catch (err) {
        return null;
    }
}

function sonido(freq=520, tipo="sine", dur=0.06, vol=0.06) {
    try {
        const audio = obtenerAudioCtx();
        if (!audio) return;

        const osc = audio.createOscillator();
        const gain = audio.createGain();

        osc.type = tipo;
        osc.frequency.value = freq;

        osc.connect(gain);
        gain.connect(audio.destination);

        const t = audio.currentTime;

        gain.gain.setValueAtTime(0.001, t);
        gain.gain.exponentialRampToValueAtTime(vol, t + 0.01);
        gain.gain.exponentialRampToValueAtTime(0.001, t + dur);

        osc.start(t);
        osc.stop(t + dur + 0.02);
    } catch (err) {}
}

["click", "touchstart", "keydown"].forEach(ev => {
    window.addEventListener(ev, () => {
        obtenerAudioCtx();
    }, {once:true, passive:false});
});

function guardarRecord() {
    const anterior = Number(localStorage.getItem("cubitos_chiringuito_record") || 0);
    if (puntos > anterior) {
        localStorage.setItem("cubitos_chiringuito_record", String(puntos));
        record = puntos;
        esNuevoRecord = true;
    } else {
        record = anterior;
        esNuevoRecord = false;
    }
}

function nuevaPartida(nivelInicial=1) {
    estado = "jugando";
    puntos = 0;
    puntosNivel = 0;
    vidas = 5;
    nivel = nivelInicial;
    rafagas = 0;
    doble = false;
    dobleHasta = 0;
    esNuevoRecord = false;
    jugador.x = 470;
    reiniciarNivel();
    enfocarCanvas();
}

function volverAlMenu() {
    estado = "menu";
    puntos = 0;
    puntosNivel = 0;
    vidas = 5;
    rafagas = 0;
    doble = false;
    dobleHasta = 0;
    cubitos = [];
    vasos = [];
    soles = [];
    limones = [];
    congeladores = [];
    particulas = [];
    salpicaduras = [];
    enfocarCanvas();
}

function pasarAlSiguienteNivel() {
    if (nivel >= 3) {
        guardarRecord();
        crearConfeti();
        estado = "victoria";
        return;
    }
    nivel++;
    puntosNivel = 0;
    rafagas = 0;
    doble = false;
    dobleHasta = 0;
    estado = "jugando";
    reiniciarNivel();
    enfocarCanvas();
}

function reiniciarNivel() {
    cubitos = [];
    vasos = [];
    soles = [];
    limones = [];
    congeladores = [];
    particulas = [];
    salpicaduras = [];
    const cantidad = nivel === 1 ? 5 : nivel === 2 ? 7 : 9;
    for (let i = 0; i < cantidad; i++) crearVaso(true);
}

function crearVaso(inicial=false) {
    const dir = Math.random() < 0.5 ? -1 : 1;
    const velBase = nivel === 1 ? 1.25 : nivel === 2 ? 1.75 : 2.25;
    vasos.push({
        x: inicial ? 125 + Math.random() * 750 : (dir > 0 ? -70 : W + 70),
        y: 250 + Math.random() * 100,
        w: 48,
        h: 70,
        vel: dir * (velBase + Math.random() * 0.75),
        lleno: 0,
        color: ["#ff5e7c", "#ffb347", "#43c6ac", "#9d77ff"][Math.floor(Math.random() * 4)]
    });
}

function lanzarCubito() {
    if (estado !== "jugando") return;
    sonido(820, "triangle", 0.055, 0.07);
    const viento = rafagas * 0.28;
    if (doble) {
        cubitos.push({x: jugador.x + 13, y: jugador.y - 12, w: 18, h: 18, vx: -0.6 + viento, vy: -10.5, giro: 0});
        cubitos.push({x: jugador.x + 34, y: jugador.y - 12, w: 18, h: 18, vx: 0.6 + viento, vy: -10.5, giro: 0});
    } else {
        cubitos.push({x: jugador.x + 25, y: jugador.y - 12, w: 18, h: 18, vx: viento, vy: -10.5, giro: 0});
    }
}

function colision(a, b) {
    return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
}

function teclaNormalizada(e) { return (e.key || "").toLowerCase(); }

function manejarTecla(e) {
    const k = teclaNormalizada(e);
    teclas[e.key] = true;
    teclas[k] = true;
    if (["Space", "Enter", "ArrowLeft", "ArrowRight"].includes(e.code) || k === "m" || e.key === "Escape") e.preventDefault();

    if (estado === "menu") {
        if (e.key === "1") elegirNivel(1);
        if (e.key === "2") elegirNivel(2);
        if (e.key === "3") elegirNivel(3);
        if (e.code === "Enter") nuevaPartida(nivelElegido);
        return;
    }
    if (estado === "jugando" && e.code === "Space") lanzarCubito();
    if (estado === "cambio_nivel") {
        if (e.code === "Enter") pasarAlSiguienteNivel();
        if (k === "m" || e.key === "Escape") volverAlMenu();
    }
    if (estado === "fin" || estado === "victoria") {
        if (k === "m" || e.key === "Escape" || e.code === "Enter") volverAlMenu();
    }
}

function soltarTecla(e) {
    const k = teclaNormalizada(e);
    teclas[e.key] = false;
    teclas[k] = false;
}
window.addEventListener("keydown", manejarTecla, {passive:false});
window.addEventListener("keyup", soltarTecla);
canvas.addEventListener("keydown", manejarTecla, {passive:false});
canvas.addEventListener("keyup", soltarTecla);

function bloquearToque(e) { if (e && e.cancelable) e.preventDefault(); }
function pulsarDireccion(tecla, activo, e) {
    bloquearToque(e);
    teclas[tecla] = activo;
    enfocarCanvas();
}
function disparoTactil(e) {
    bloquearToque(e);
    enfocarCanvas();
    lanzarCubito();
}

btnLeft.addEventListener("touchstart", e => pulsarDireccion("ArrowLeft", true, e), {passive:false});
btnLeft.addEventListener("touchend", e => pulsarDireccion("ArrowLeft", false, e), {passive:false});
btnLeft.addEventListener("touchcancel", e => pulsarDireccion("ArrowLeft", false, e), {passive:false});
btnLeft.addEventListener("mousedown", e => pulsarDireccion("ArrowLeft", true, e));
btnLeft.addEventListener("mouseup", e => pulsarDireccion("ArrowLeft", false, e));
btnLeft.addEventListener("mouseleave", e => pulsarDireccion("ArrowLeft", false, e));

btnRight.addEventListener("touchstart", e => pulsarDireccion("ArrowRight", true, e), {passive:false});
btnRight.addEventListener("touchend", e => pulsarDireccion("ArrowRight", false, e), {passive:false});
btnRight.addEventListener("touchcancel", e => pulsarDireccion("ArrowRight", false, e), {passive:false});
btnRight.addEventListener("mousedown", e => pulsarDireccion("ArrowRight", true, e));
btnRight.addEventListener("mouseup", e => pulsarDireccion("ArrowRight", false, e));
btnRight.addEventListener("mouseleave", e => pulsarDireccion("ArrowRight", false, e));

btnShoot.addEventListener("touchstart", disparoTactil, {passive:false});
btnShoot.addEventListener("mousedown", disparoTactil);
btnMenu.addEventListener("click", volverAlMenu);
btnStart.addEventListener("click", () => {
    if (estado === "menu") nuevaPartida(nivelElegido);
    else if (estado === "cambio_nivel") pasarAlSiguienteNivel();
    else if (estado === "fin" || estado === "victoria") volverAlMenu();
    enfocarCanvas();
});

function texto(txt, y, color="#063f5e", size=26, bold=false) {
    ctx.fillStyle = color;
    ctx.font = `${bold ? "bold " : ""}${size}px Trebuchet MS, Verdana, Arial`;
    ctx.textAlign = "center";
    ctx.fillText(txt, W / 2, y);
}

function cajaTexto(x, y, w, h, color, borde="#075c7d") {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, w, h);
    ctx.strokeStyle = borde;
    ctx.lineWidth = 4;
    ctx.strokeRect(x, y, w, h);
}

function fondoChiringuito() {
    const grad = ctx.createLinearGradient(0, 0, 0, H);
    grad.addColorStop(0, "#79d9ff");
    grad.addColorStop(0.47, "#b7f1ff");
    grad.addColorStop(0.48, "#4fbbe7");
    grad.addColorStop(0.62, "#1092c4");
    grad.addColorStop(0.63, "#f3d28b");
    grad.addColorStop(1, "#d99b46");
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, W, H);

    ctx.fillStyle = "rgba(255,255,255,0.55)";
    for (let x = -60; x < W + 80; x += 130) {
        const y = 292 + Math.sin((frame + x) * 0.025) * 5;
        ctx.beginPath();
        ctx.ellipse(x, y, 55, 8, 0, 0, Math.PI * 2);
        ctx.fill();
    }

    dibujarSolFondo();
    dibujarPalmera(72, 355, 1.08, -1);
    dibujarPalmera(923, 350, 1.0, 1);

    ctx.fillStyle = "#8b5225";
    ctx.fillRect(70, 385, 860, 110);
    ctx.fillStyle = "#b87535";
    ctx.fillRect(70, 365, 860, 38);
    ctx.fillStyle = "#5d3318";
    ctx.fillRect(70, 400, 860, 10);

    for (let x = 115; x < 910; x += 85) {
        ctx.fillStyle = "rgba(255,255,255,0.18)";
        ctx.fillRect(x, 369, 36, 26);
    }
}

function dibujarSolFondo() {
    ctx.fillStyle = "#ffe45e";
    ctx.beginPath();
    ctx.arc(845, 80, 42, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = "rgba(255, 198, 45, 0.8)";
    ctx.lineWidth = 4;
    for (let i = 0; i < 12; i++) {
        const a = i * Math.PI / 6 + frame * 0.004;
        ctx.beginPath();
        ctx.moveTo(845 + Math.cos(a) * 52, 80 + Math.sin(a) * 52);
        ctx.lineTo(845 + Math.cos(a) * 70, 80 + Math.sin(a) * 70);
        ctx.stroke();
    }
}

function dibujarPalmera(x, y, s, lado) {
    ctx.save();
    ctx.translate(x, y);
    ctx.scale(s * lado, s);
    ctx.rotate(Math.sin(frame * 0.02 + x) * 0.035);
    ctx.fillStyle = "#8b5a2b";
    ctx.fillRect(-12, -130, 24, 145);
    ctx.fillStyle = "#1f8b4c";
    for (let i = 0; i < 7; i++) {
        const a = -Math.PI * 0.95 + i * Math.PI * 0.32 + Math.sin(frame * 0.018) * 0.06;
        ctx.beginPath();
        ctx.ellipse(Math.cos(a) * 42, -142 + Math.sin(a) * 26, 64, 13, a, 0, Math.PI * 2);
        ctx.fill();
    }
    ctx.fillStyle = "#6b3f1e";
    ctx.beginPath();
    ctx.arc(0, -132, 13, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
}

function dibujarCamarero() {
    const x = jugador.x;
    const y = jugador.y;
    ctx.fillStyle = "#f2bf92";
    ctx.beginPath();
    ctx.arc(x + 29, y + 10, 16, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(x + 11, y + 26, 36, 28);
    ctx.fillStyle = "#075c7d";
    ctx.fillRect(x + 15, y + 33, 28, 9);
    ctx.strokeStyle = "#07364d";
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(x + 14, y + 54);
    ctx.lineTo(x + 7, y + 70);
    ctx.moveTo(x + 44, y + 54);
    ctx.lineTo(x + 52, y + 70);
    ctx.moveTo(x + 14, y + 33);
    ctx.lineTo(x - 2, y + 45);
    ctx.moveTo(x + 45, y + 33);
    ctx.lineTo(x + 61, y + 45);
    ctx.stroke();
    ctx.fillStyle = "#07364d";
    ctx.fillRect(x + 10, y - 11, 38, 8);
    ctx.fillRect(x + 18, y - 22, 22, 12);
}

function dibujarVaso(v) {
    ctx.save();
    ctx.translate(v.x + v.w / 2, v.y + v.h / 2);
    ctx.rotate(Math.sin(frame * 0.035 + v.x) * 0.04);
    ctx.translate(-v.w / 2, -v.h / 2);

    ctx.fillStyle = "rgba(255,255,255,0.52)";
    ctx.beginPath();
    ctx.moveTo(7, 0);
    ctx.lineTo(v.w - 7, 0);
    ctx.lineTo(v.w - 13, v.h);
    ctx.lineTo(13, v.h);
    ctx.closePath();
    ctx.fill();
    ctx.strokeStyle = "#d8f6ff";
    ctx.lineWidth = 3;
    ctx.stroke();

    const alto = Math.min(v.h - 11, v.lleno * 18);
    ctx.fillStyle = v.color;
    ctx.fillRect(13, v.h - 7 - alto, v.w - 26, alto);

    ctx.fillStyle = "rgba(255,255,255,0.75)";
    ctx.fillRect(17, 10, 7, 42);
    ctx.restore();
}

function dibujarCubito(c) {
    ctx.save();
    ctx.translate(c.x + c.w / 2, c.y + c.h / 2);
    ctx.rotate(c.giro);
    ctx.fillStyle = "rgba(220, 250, 255, 0.95)";
    ctx.fillRect(-c.w / 2, -c.h / 2, c.w, c.h);
    ctx.strokeStyle = "#78dfff";
    ctx.lineWidth = 2;
    ctx.strokeRect(-c.w / 2, -c.h / 2, c.w, c.h);
    ctx.fillStyle = "rgba(255,255,255,0.9)";
    ctx.fillRect(-4, -6, 5, 5);
    ctx.restore();
}

function dibujarSolPenalizador(s) {
    ctx.fillStyle = "#ffde45";
    ctx.beginPath();
    ctx.arc(s.x + 18, s.y + 18, 17, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = "#ff8c1a";
    ctx.lineWidth = 3;
    for (let i = 0; i < 8; i++) {
        const a = i * Math.PI / 4 + frame * 0.05;
        ctx.beginPath();
        ctx.moveTo(s.x + 18 + Math.cos(a) * 21, s.y + 18 + Math.sin(a) * 21);
        ctx.lineTo(s.x + 18 + Math.cos(a) * 28, s.y + 18 + Math.sin(a) * 28);
        ctx.stroke();
    }
}

function dibujarBonus(b, tipo) {
    if (tipo === "limon") {
        ctx.fillStyle = "#d5ef35";
        ctx.beginPath();
        ctx.ellipse(b.x + 16, b.y + 16, 18, 12, -0.5, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#819b16";
        ctx.stroke();
    } else {
        ctx.fillStyle = "#72e8ff";
        ctx.beginPath();
        ctx.arc(b.x + 16, b.y + 16, 17, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 18px Trebuchet MS, Verdana, Arial";
        ctx.textAlign = "center";
        ctx.fillText("2", b.x + 16, b.y + 23);
    }
}

function crearSalpicadura(x, y, color="#bff7ff") {
    sonido(420, "sine", 0.06, 0.06);
    for (let i = 0; i < 13; i++) {
        salpicaduras.push({
            x, y,
            vx: (Math.random() - 0.5) * 5,
            vy: -Math.random() * 4 - 1,
            g: 0.18,
            vida: 30 + Math.random() * 15,
            color,
            tam: 2 + Math.random() * 3
        });
    }
}

function crearConfeti() {
    particulas = [];
    const colores = ["#ffffff", "#72e8ff", "#ffe45e", "#20ad6b", "#ff5e7c"];
    for (let i = 0; i < 100; i++) {
        particulas.push({
            x: W / 2,
            y: 190,
            vx: (Math.random() - 0.5) * 9,
            vy: -Math.random() * 7 - 2,
            g: 0.16,
            vida: 70 + Math.random() * 40,
            color: colores[Math.floor(Math.random() * colores.length)],
            tam: 3 + Math.random() * 5
        });
    }
    sonido(660, "triangle", 0.12, 0.08);
}

function actualizarParticulas() {
    particulas.forEach(p => { p.x += p.vx; p.y += p.vy; p.vy += p.g; p.vida--; });
    particulas = particulas.filter(p => p.vida > 0);
    salpicaduras.forEach(p => { p.x += p.vx; p.y += p.vy; p.vy += p.g; p.vida--; });
    salpicaduras = salpicaduras.filter(p => p.vida > 0);
}

function dibujarParticulas() {
    [...particulas, ...salpicaduras].forEach(p => {
        ctx.globalAlpha = Math.max(0, Math.min(1, p.vida / 35));
        ctx.fillStyle = p.color;
        ctx.fillRect(p.x, p.y, p.tam, p.tam);
        ctx.globalAlpha = 1;
    });
}

function actualizar() {
    frame++;
    actualizarParticulas();
    if (estado !== "jugando") return;

    if (teclas["ArrowLeft"] && jugador.x > 96) jugador.x -= jugador.vel;
    if (teclas["ArrowRight"] && jugador.x + jugador.w < W - 96) jugador.x += jugador.vel;

    if (doble && Date.now() > dobleHasta) doble = false;

    if (Math.random() < (nivel === 1 ? 0.006 : nivel === 2 ? 0.011 : 0.017)) {
        const dir = Math.random() < 0.5 ? -1 : 1;
        rafagas = dir * (nivel === 1 ? 2.0 : nivel === 2 ? 3.0 : 4.2);
        setTimeout(() => { rafagas = 0; }, 1200 + Math.random() * 800);
    }

    cubitos.forEach(c => {
        c.x += c.vx + rafagas * 0.04;
        c.y += c.vy;
        c.vy += 0.08;
        c.giro += 0.09;
    });
    cubitos = cubitos.filter(c => c.y > -35 && c.x > 65 && c.x < W - 65);

    vasos.forEach(v => {
        v.x += v.vel;
        if (v.x < 95 || v.x + v.w > W - 95) {
            v.vel *= -1;
            v.y += nivel === 1 ? 5 : nivel === 2 ? 7 : 9;
        }
        if (v.y > 382) {
            vidas--;
            v.x = 130 + Math.random() * 760;
            v.y = 245;
            v.lleno = 0;
        }
    });

    const probSol = nivel === 1 ? 0.004 : nivel === 2 ? 0.008 : 0.012;
    if (Math.random() < probSol) soles.push({x: 120 + Math.random() * 760, y: 60, w: 36, h: 36, vy: 2 + nivel * 0.6});
    soles.forEach(s => s.y += s.vy);
    soles = soles.filter(s => {
        if (colision(s, jugador)) { vidas--; sonido(160, "sawtooth", 0.08, 0.05); return false; }
        return s.y < H;
    });

    if (Math.random() < 0.0035) limones.push({x: 120 + Math.random() * 760, y: 80, w: 32, h: 32, vy: 2.2});
    if (Math.random() < 0.0025) congeladores.push({x: 120 + Math.random() * 760, y: 80, w: 32, h: 32, vy: 2.2});
    limones.forEach(b => b.y += b.vy);
    congeladores.forEach(b => b.y += b.vy);

    limones = limones.filter(b => {
        if (colision(b, jugador)) { puntos += 5; crearSalpicadura(b.x + 16, b.y + 16, "#d5ef35"); return false; }
        return b.y < H;
    });
    congeladores = congeladores.filter(b => {
        if (colision(b, jugador)) { doble = true; dobleHasta = Date.now() + 10000; crearSalpicadura(b.x + 16, b.y + 16); return false; }
        return b.y < H;
    });

    cubitos.forEach(c => {
        soles.forEach(s => {
            if (!c.muerto && colision(c, s)) {
                c.muerto = true;
                s.muerto = true;
                crearSalpicadura(c.x, c.y, "#ffffff");
            }
        });
        vasos.forEach(v => {
            if (!c.muerto && colision(c, v)) {
                c.muerto = true;
                v.lleno++;
                puntos++;
                crearSalpicadura(c.x + 9, c.y + 9, "#bff7ff");
                if (v.lleno >= 3) {
                    puntosNivel++;
                    puntos += 2;
                    crearSalpicadura(v.x + 24, v.y + 20, v.color);
                    v.x = 130 + Math.random() * 760;
                    v.y = 240 + Math.random() * 80;
                    v.lleno = 0;
                    if (Math.random() < 0.22 && vasos.length < 13) crearVaso(false);
                }
            }
        });
    });

    cubitos = cubitos.filter(c => !c.muerto);
    soles = soles.filter(s => !s.muerto);

    if (vidas <= 0) {
        guardarRecord();
        estado = "fin";
        return;
    }

    if (puntosNivel >= objetivoNivel()) {
        if (nivel >= 3) {
            guardarRecord();
            crearConfeti();
            estado = "victoria";
        } else {
            mensajeNivel = nivel === 1 ? "Nivel 1 superado" : "Nivel 2 superado";
            crearConfeti();
            estado = "cambio_nivel";
        }
    }
}

function dibujarHUD() {
    cajaTexto(108, 12, 784, 56, "rgba(255,248,215,0.9)", "#075c7d");
    ctx.textAlign = "left";
    ctx.font = "bold 21px Trebuchet MS, Verdana, Arial";
    ctx.fillStyle = "#063f5e";
    ctx.fillText(`Puntos: ${puntos}`, 130, 46);
    ctx.fillText(`Vidas: ${vidas}`, 285, 46);
    ctx.fillText(`Nivel: ${nivel}`, 410, 46);
    ctx.fillText(`Vasos: ${puntosNivel}/${objetivoNivel()}`, 525, 46);
    ctx.textAlign = "right";
    ctx.fillText(`🏆 ${record}`, 870, 46);
    if (doble) {
        const quedan = Math.max(0, Math.ceil((dobleHasta - Date.now()) / 1000));
        ctx.fillStyle = "#20ad6b";
        ctx.fillText(`🧊x2 ${quedan}s`, 765, 66);
    }
    if (rafagas !== 0) {
        ctx.fillStyle = "#075c7d";
        ctx.fillText(rafagas > 0 ? "🌬️ Viento →" : "🌬️ Viento ←", 870, 66);
    }
}

function dibujarMenu() {
    fondoChiringuito();
    cajaTexto(145, 82, 710, 365, "rgba(255,248,215,0.94)", "#075c7d");
    texto("🧊 CUBITOS AL CHIRINGUITO 🧊", 140, "#075c7d", 33, true);
    texto("Llena los vasos antes de que el verano los caliente", 183, "#136f91", 22);
    texto(`Nivel elegido: ${nivelElegido}`, 230, "#20ad6b", 30, true);
    texto(`🏆 Récord: ${record}`, 262, "#075c7d", 22, true);
    texto("1  Brisa suave: vasos lentos y poco sol", 302, "#063f5e", 21);
    texto("2  Mediodía: más viento y más calor", 337, "#063f5e", 21);
    texto("3  Agosto infernal: chiringuito a tope", 372, "#063f5e", 21);
    texto("Soles derriten cubitos. El viento desvía el tiro.", 414, "#d87800", 21, true);
    texto("ENTER PARA COMENZAR", 516, "#20ad6b", 30, true);
}

function dibujarJuego() {
    fondoChiringuito();
    vasos.forEach(dibujarVaso);
    cubitos.forEach(dibujarCubito);
    soles.forEach(dibujarSolPenalizador);
    limones.forEach(b => dibujarBonus(b, "limon"));
    congeladores.forEach(b => dibujarBonus(b, "congelador"));
    dibujarCamarero();
    dibujarParticulas();
    dibujarHUD();
}

function dibujarCambioNivel() {
    fondoChiringuito();
    dibujarParticulas();
    cajaTexto(160, 150, 680, 275, "rgba(255,248,215,0.95)", "#075c7d");
    texto(mensajeNivel, 220, "#20ad6b", 40, true);
    texto(`Puntuación total: ${puntos}`, 275, "#063f5e", 26);
    texto(`Vidas restantes: ${vidas}`, 313, "#063f5e", 24);
    texto(`¿Pasamos al nivel ${nivel + 1}?`, 365, "#075c7d", 30, true);
    texto("ENTER: continuar    M: menú", 405, "#20ad6b", 23, true);
}

function dibujarFinal() {
    fondoChiringuito();
    dibujarParticulas();
    cajaTexto(175, 165, 650, 250, "rgba(255,248,215,0.95)", "#075c7d");
    if (estado === "fin") {
        texto("SE DERRITIÓ EL CHIRINGUITO", 240, "#d87800", 37, true);
    } else {
        texto("🏖️ ¡VERANO REFRESCADO! 🏖️", 240, "#20ad6b", 39, true);
    }
    texto(`Puntuación final: ${puntos}`, 300, "#063f5e", 28);
    texto(`🏆 Récord: ${record}`, 338, "#075c7d", 23, true);
    if (esNuevoRecord) texto("🎉 ¡NUEVO RÉCORD! 🎉", 374, "#20ad6b", 26, true);
    texto("Pulsa M, ESC o ENTER para volver al menú", 404, "#20ad6b", 21, true);
}

function dibujar() {
    if (estado === "menu") dibujarMenu();
    else if (estado === "jugando") dibujarJuego();
    else if (estado === "cambio_nivel") dibujarCambioNivel();
    else dibujarFinal();
}

function loop() {
    actualizar();
    dibujar();
    requestAnimationFrame(loop);
}
loop();
</script>
""", height=760, scrolling=False)
