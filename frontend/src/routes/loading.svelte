<svelte>

</svelte>

<div class="loading-container">
    <div class="loading-text text-amber-950">
        <span>F</span>
        <span>R</span>
        <span>E</span>
        <span>S</span>
        <span>H</span>
        <span>K</span>
        <span>E</span>
        <span>E</span>
        <span>P</span>
    </div>
</div>

<style>
    .loading-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        background-color: #F2EDE3;
    }
    .loading-text {
        font-size: 3rem;
        font-family: 'Grandstander', cursive;
        display: flex;
    }
    .loading-text span {
        opacity: 0;
        animation: fadeInOut 1s infinite;
        animation-fill-mode: both;
    }
    .loading-text span:nth-child(1) {
        animation-delay: 0s;
    }
    .loading-text span:nth-child(2) {
        animation-delay: 0.1s;
    }
    .loading-text span:nth-child(3) {
        animation-delay: 0.2s;
    }
    .loading-text span:nth-child(4) {
        animation-delay: 0.3s;
    }
    .loading-text span:nth-child(5) {
        animation-delay: 0.4s;
    }
    .loading-text span:nth-child(6) {
        animation-delay: 0.5s;
    }
    .loading-text span:nth-child(7) {
        animation-delay: 0.6s;
    }
    .loading-text span:nth-child(8) {
        animation-delay: 0.7s;
    }
    .loading-text span:nth-child(9) {
        animation-delay: 0.8s;
    }
    @keyframes fadeInOut {
        0% {
            opacity: 0;
        }
        50% {
            opacity: 1;
        }
        100% {
            opacity: 0;
        }
    }
</style>