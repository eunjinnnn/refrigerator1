<!-- Modal.svelte -->
<script>
    export let food;
    export let close;
</script>

{#if food}
<div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 modal">
    <div class="bg-white rounded-lg p-4 w-1/2 modal-content">
        <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg font-semibold">Food Details</h2>
            <button on:click={close} class="text-red-500">&times;</button>
        </div>
        <p><strong>Name:</strong> {food.foodname}</p>
        <p><strong>Volume:</strong> {food.volume} {food.unit}</p>
        <p><strong>Expiration Date:</strong> {food.expiration_date}</p>
    </div>
</div>
{/if}

<style>
    .modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .modal-content {
        background: white;
        padding: 20px;
        border-radius: 8px;
        position: relative;
    }
</style>
