document.addEventListener('DOMContentLoaded', function() {
    const speakButton = document.getElementById('speak-button');
    const stopButton = document.getElementById('stop-button');
    const answerList = document.getElementById('answer-list');
    const voiceSelect = document.getElementById('voice-select');
    let voices = [];

    function populateVoiceList() {
        voices = window.speechSynthesis.getVoices();
        voiceSelect.innerHTML = '';
        voices.forEach(voice => {
            const option = document.createElement("option");
            option.textContent = `${voice.name} (${voice.lang})`;
            option.value = voice.name;
            voiceSelect.appendChild(option);
        });
    }

    populateVoiceList();
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
        window.speechSynthesis.onvoiceschanged = populateVoiceList;
    }

    if (speakButton && answerList) {
        speakButton.addEventListener('click', function() {
            const items = answerList.querySelectorAll('li');
            let text = '';
            items.forEach(item => {
              text += item.textContent + '. ';
            });
            speakText(text);
        });
    }

    if (stopButton) {
        stopButton.addEventListener('click', function() {
            window.speechSynthesis.cancel();
        });
    }

    function speakText(text) {
        const synth = window.speechSynthesis;

        if (synth.speaking) {
            console.error('speechSynthesis.speaking');
            return;
        }

        const utterThis = new SpeechSynthesisUtterance(text);

        utterThis.onend = function(event) {
            console.log('SpeechSynthesisUtterance.onend');
        }

        utterThis.onerror = function(event) {
            console.error('SpeechSynthesisUtterance.onerror');
        }

        // Voice Selection
        const selectedVoiceName = voiceSelect.value;
        const selectedVoice = voices.find(voice => voice.name === selectedVoiceName);
        if (selectedVoice) {
            utterThis.voice = selectedVoice;
        }

        utterThis.pitch = 1;
        utterThis.rate = 1;
        utterThis.lang = 'en-US';

        synth.speak(utterThis);
    }
});