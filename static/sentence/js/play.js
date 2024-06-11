    document.addEventListener('DOMContentLoaded', function() {
        nextSentence();
    });

    (function() {
        const sentenceElement = document.getElementById('sentence');
        const audio = document.getElementById('audioPlayer');
        const translateText = document.getElementById('translate');
        const originText = document.getElementById('origin_text');
        const countPage = document.getElementById('count_page');
        const answer = document.getElementById('answer');
        const dataAll = JSON.parse(document.getElementById('data-all').getAttribute('data-all'));

        if (!sentenceElement || !audio || !translateText || !originText || !countPage || !answer || !dataAll) {
            console.error('Some elements or data are missing.');
            return;
        }

        let dataAllCopy = [...dataAll];
        let globalRandomIndex = 0;

        function nextSentence() {
            translateText.style.display = 'none';
            originText.style.display = 'none';

            if (dataAllCopy.length === 0) {
                sentenceElement.innerText = 'Done';
            } else {
                const randomIndex = Math.floor(Math.random() * dataAllCopy.length);
                globalRandomIndex = randomIndex;
                const sentence = dataAllCopy[randomIndex];

                sentenceElement.innerText = sentence.fields.text;
                audio.src = `/media/${sentence.fields.audio}`;
                translateText.innerText = sentence.fields.text_translate;
                originText.innerText = sentence.fields.text;
                countPage.innerText = `${dataAll.length}/${dataAllCopy.length}`;
                dataAllCopy.splice(randomIndex, 1);
                answer.innerText = '';
            }
        }

        function audioPlay() {
            audio.play();
        }

        function checking() {
            const textOrigin = sentenceElement.innerText;
            const userInput = document.getElementById('user_input').value;
            if (textOrigin.trim().toLowerCase() === userInput.trim().toLowerCase()) {
                answer.innerText = 'Correct';
            }
        }

        function showTranslate() {
            translateText.style.display = 'block';
        }

        function showOriginText() {
            originText.style.display = 'block';
        }
function clearInput() {
    document.getElementById('user_input').value = '';
}


        window.nextSentence = nextSentence;
        window.audioPlay = audioPlay;
        window.checking = checking;
        window.showTranslate = showTranslate;
        window.showOriginText = showOriginText;
        window.clearInput = clearInput;
    })();