let mediaRecorder;
let audioChunks = [];
const recordBtn = document.getElementById('recordBtn');
const stopBtn = document.getElementById('stopBtn');
const recordingsList = document.getElementById('recordingsList');
const canvas = document.getElementById('audioCanvas');
const canvasCtx = canvas.getContext('2d');
let audioCtx;
let analyser;
let dataArray;
let source;

recordBtn.addEventListener('click', async () => {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        startRecording(stream);
    } catch (err) {
        console.error('Error accessing microphone:', err);
        alert('Could not access microphone. Please ensure permission is granted.');
    }
});

stopBtn.addEventListener('click', () => {
    mediaRecorder.stop();
    recordBtn.disabled = false;
    stopBtn.disabled = true;
    // Stop visualization
    cancelAnimationFrame(drawVisual);
    // Stop all tracks to release microphone
    mediaRecorder.stream.getTracks().forEach(track => track.stop());
});

function startRecording(stream) {
    mediaRecorder = new MediaRecorder(stream);
    audioChunks = [];

    // Setup Visualization
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    analyser = audioCtx.createAnalyser();
    source = audioCtx.createMediaStreamSource(stream);
    source.connect(analyser);
    analyser.fftSize = 256;
    dataArray = new Uint8Array(analyser.frequencyBinCount);

    visualize();

    mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
    };

    mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const audioUrl = URL.createObjectURL(audioBlob);
        const audio = document.createElement('audio');
        audio.src = audioUrl;
        audio.controls = true;
        const item = document.createElement('div');
        item.style.marginTop = "10px";
        item.appendChild(audio);
        recordingsList.appendChild(item);
    };

    mediaRecorder.start();
    recordBtn.disabled = true;
    stopBtn.disabled = false;
}

let drawVisual;
function visualize() {
    const WIDTH = canvas.width;
    const HEIGHT = canvas.height;

    function draw() {
        drawVisual = requestAnimationFrame(draw);

        analyser.getByteFrequencyData(dataArray);

        canvasCtx.fillStyle = 'rgb(0, 0, 0)';
        canvasCtx.fillRect(0, 0, WIDTH, HEIGHT);

        const barWidth = (WIDTH / dataArray.length) * 2.5;
        let barHeight;
        let x = 0;

        for (let i = 0; i < dataArray.length; i++) {
            barHeight = dataArray[i] / 2;

            canvasCtx.fillStyle = `rgb(${barHeight + 100}, 50, 50)`;
            canvasCtx.fillRect(x, HEIGHT - barHeight, barWidth, barHeight);

            x += barWidth + 1;
        }
    }

    draw();
}