<script>
    import { Button, Label, Input, Select } from 'flowbite-svelte';
    export let food;
    export let close;
    export let deleteFood;
    export let showEditForm;
    export let categories; // 카테고리 리스트
    export let units; // 단위 리스트

    let showEditModal = false;

    function getCategoryName(categoryId) {
        const category = categories.find(cat => cat.id === categoryId);
        return category ? category.name : 'Unknown';
    }

    function getUnitName(unitId) {
        const unit = units.find(unit => unit.id === unitId);
        return unit ? unit.name : '';
    }

    function openEditModal() {
        showEditModal = true;
    }

    function closeEditModal() {
        showEditModal = false;
    }
</script>

{#if food}
<div class="modal active">
    <div class="bg-orange-50 rounded-lg p-4 w-1/2 modal-content" style="background-color: #FFFBF6;">
        <div class="flex justify-between items-center mb-2">
            <h2 class="text-lg font-grandstander ml-1"><strong>Food Details</strong></h2>
            <button on:click={close} class="text-lime-950 text-lg flex items-center ">&times;</button>
        </div>
        <div class="border-b border-zinc-950 border-opacity-30 mb-2"></div>
        <!-- <div class="flex justify-between items-center mb-2">
            <h2 class="text-lg text-lime-950 font-PoetsenOne"><strong>{food.foodname} {food.volume} {getUnitName(food.unit_id)}</strong></h2>
            <button on:click={close} class="text-lime-950 text-lg flex items-center ">&times;</button>
        </div> -->
        <!-- <div class="border-b border-lime-950 border-opacity-30 mb-2"></div> -->

        <p class='font-grandstander mb-1'>Food Name: <span class='font-PoetsenOne'>{food.foodname}</span></p>
        <p class='font-grandstander mb-1'>Food volume: <span class='font-PoetsenOne'>{food.volume}{getUnitName(food.unit_id)} </span></p>
        <p class='font-grandstander mb-1'>Category: <span class='font-PoetsenOne'>{getCategoryName(food.category_id)}</span></p>
        <p class='font-grandstander mb-1'>Purchase Date: <span class='font-PoetsenOne'>{food.purchase_date}</span></p>
        <p class='font-grandstander mb-1'>Expiration Date: <span class='font-PoetsenOne'>{food.expiration_date}</span></p>
        <div class='flex justify-between pt-2'>
            <Button type="button" on:click={() => deleteFood(food)} class="flex border-[1px] border-zinc-500 text-xxs font-semibold font-PoetsenOne  bg-[#E8C9D5]/50 text-zinc-950 hover:bg-[#E8C9D5]" size='xs'>DELETE</Button>
            <Button type="button" on:click={() => showEditForm(food)} class="flex border-[1px] border-zinc-500 text-xxs font-semibold font-PoetsenOne  bg-[#E8C9D5]/50 text-zinc-950 hover:bg-[#E8C9D5]" size='xs'>EDIT</Button>
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
