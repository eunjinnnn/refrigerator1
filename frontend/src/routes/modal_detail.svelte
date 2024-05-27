<script>
    export let food;
    export let close;
</script>

{#if food}
<div class="modal {food ? 'active' : ''}">
    <div class="bg-white rounded-lg p-4 w-1/2 modal-content">
        <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg font-semibold">{food.foodname}</h2>
            <button on:click={close} class="text-red-500">&times;</button>
        </div>
        <p><strong>Name:</strong> {food.foodname}</p>
        <p><strong>Volume:</strong> {food.volume} {food.unit}</p>
        <p><strong>Expiration Date:</strong> {food.expiration_date}</p>
    </div>
</div>
{/if}

<!-- <div class="modal {food ? 'active' : ''}">
    <div class="modal-content">
        <form>
            <div>hi</div>
            <button on:click={close} class="text-red-500">&times;</button>
        </form>
    </div>
</div> -->

<style>
    .modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        visibility: hidden;
        opacity: 0;
        transition: visibility 0s, opacity 0.5s linear;
    }
    .modal.active {
        visibility: visible;
        opacity: 1;
    }
    .modal-content {
        background: white;
        padding: 20px;
        border-radius: 8px;
        width: 80%;
        max-width: 500px;
    }
</style>

