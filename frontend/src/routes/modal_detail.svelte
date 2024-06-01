<script>
    import { Button } from 'flowbite-svelte';
    export let food;
    export let close;
    export let deleteFood;
    export let showEditForm;

    let categories = [
        { id: 1, name: 'VEGETABLES' },
        { id: 2, name: 'DRINKS' },
        { id: 3, name: 'FROZEN FOOD' },
        { id: 4, name: 'ETC' }
    ];

    // food.category ID에 해당하는 카테고리 이름을 가져오는 함수
    function getCategoryName(categoryId) {
        const category = categories.find(cat => cat.id === categoryId);
        return category ? category.name : 'Unknown';
    }
</script>

{#if food}
<div class="modal {food ? 'active' : ''}">
    <div class="bg-orange-50 rounded-lg p-4 w-1/2 modal-content">
        <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg text-lime-950 font-PoetsenOne"><strong>{food.foodname} {food.volume}{food.unit}</strong></h2>
            <button on:click={close} class="text-lime-950 text-lg flex items-center ">&times;</button>
        </div>

        <div class="border-b border-lime-950 border-opacity-30 mb-2"></div>
        <p class='font-PoetsenOne'><strong>Category:</strong> {getCategoryName(food.category)}</p>
        <p class='font-PoetsenOne'><strong>Expiration Date:</strong> {food.expiration_date}</p>
        <p class='font-PoetsenOne'><strong>Purchase Date:</strong> {food.purchase_date}</p>
        <div class='flex justify-between mt-2'>
            <Button type="button" on:click={() => deleteFood(food)} class="flex font-PoetsenOne text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>DELETE</Button>
            <Button type="button" on:click={() => editFood(food)} class="flex font-PoetsenOne text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>EDIT</Button>
        </div>
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
