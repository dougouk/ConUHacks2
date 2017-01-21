var audioContext = new (window.AudioContext || window.webkitAudioContext)();
var audioPlayer = new AudioPlayer(audioContext);

function AudioPlayer(audioContext) {
    var isPlaying = false;
    var context = audioContext;
    var source = null;

    this.isPlaying = function () {
        return isPlaying;
    };

    this.play = function (audio) {
        var audioToPlay = new Int16Array(audio);
        source = context.createBufferSource();
        var audioBuffer = context.createBuffer(1, audioToPlay.length, 8000);
        var channelData = audioBuffer.getChannelData(0);
        for (var i = 0; i < channelData.length; ++i)
        {
            channelData[i] = audioToPlay[i] / 32768.0;
        }
        source.buffer = audioBuffer;
        source.connect(context.destination);
        if (source.start) {
            source.start(0);
        }
        else {
            source.noteOn(0);
        }
        isPlaying = true;

        source.onended = function ()
        {
            isPlaying = false;
        };
    };

    this.stop = function () {
        if (source != null) {
            source.stop();
            isPlaying = false;
        }
    }
}

function playAudio(text) {
    var request = new XMLHttpRequest();

    request.open("POST", '/tts', true);
    request.setRequestHeader("Content-type", "application/json");
    request.responseType = "arraybuffer";

    request.send(JSON.stringify({
        text: text,
    }));

    request.onreadystatechange = function(event) {
        if (request.readyState === 4 && request.status === 200) {
            var arrayBuffer = request.response;
            if (arrayBuffer) {
                audioPlayer.play(arrayBuffer);
            }
        }
    };
}

$(document).ready(function() {
    playAudio("welcome");
});
