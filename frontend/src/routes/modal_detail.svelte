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
    <div class="bg-orange-50 rounded-lg p-4 w-1/2 modal-content">
        <div class="flex justify-between items-center mb-2">
            <h2 class="text-lg text-lime-950 font-PoetsenOne"><strong>{food.foodname} {food.volume} {getUnitName(food.unit_id)}</strong></h2>
            <button on:click={close} class="text-lime-950 text-lg flex items-center ">&times;</button>
        </div>

        <div class="border-b border-lime-950 border-opacity-30 mb-2"></div>
        <p class='font-PoetsenOne'><strong>Category:</strong> {getCategoryName(food.category_id)}</p>
        <p class='font-PoetsenOne'><strong>Purchase Date:</strong> {food.purchase_date}</p>
        <p class='font-PoetsenOne'><strong>Expiration Date:</strong> {food.expiration_date}</p>
        <div class='flex justify-between mt-2'>
            <Button type="button" on:click={() => deleteFood(food)} class="flex font-PoetsenOne text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>DELETE</Button>
            <Button type="button" on:click={() => showEditForm(food)} class="flex font-PoetsenOne text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>EDIT</Button>
        </div>
    </div>
</div>
{/if}

<!-- {#if showEditModal}
<div class="modal active">
    <div class="bg-orange-50 rounded-lg p-4 w-1/2 modal-content">
        <div class="flex justify-between items-center mb-2">
            <h2 class="text-lg text-lime-950 font-PoetsenOne"><strong>Edit Food</strong></h2>
            <button on:click={closeEditModal} class="text-lime-950 text-lg flex items-center ">&times;</button>
        </div>

        <div class="border-b border-lime-950 border-opacity-30 mb-2"></div>

        <form on:submit={editFood}>
            <div class="flex flex-col mt-2 p-2">
                <label for="category" class="flex font-PoetsenOne">Category</label>
                <select id="category" bind:value={food.category_id} class="flex w-full p-2 mt-1 border-opacity-30" style='border-radius: 8px;'>
                    {#each categories as category}
                        <option value={category.id}>{category.name}</option>
                    {/each}
                </select>
            </div>
            <div class='flex flex-wrap'>
                <div class='flex flex-col w-1/3 p-2'>
                    <label for="foodname" class="flex font-PoetsenOne">Food Name</label>
                    <input type="text" bind:value={food.foodname} class='flex font-PoetsenOne mt-1' style='border-radius: 8px;' id="foodname" placeholder="Foodname" required/>
                </div>
                <div class="flex flex-col w-1/3 p-2">
                    <label for="volume" class="flex font-PoetsenOne">Volume</label>
                    <input type="number" id="volume" bind:value={food.volume} style='border-radius: 8px;' class="flex font-PoetsenOne mt-1"/>
                </div>
                <div class="flex flex-col w-1/3 p-2">
                    <label for="unit" class="flex font-PoetsenOne">Unit</label>
                    <select id="unit" bind:value={food.unit_id} style='border-radius: 8px;' class="flex font-PoetsenOne mt-1">
                        {#each units as unit}
                            <option value={unit.id}>{unit.name}</option>
                    {/each}
                    </select>
                </div>
            </div>
            <div class="flex flex-wrap">
                <div class="flex flex-col w-1/2 p-2">
                    <label for="expiration_date" class="font-PoetsenOne">Expiration Date</label>
                    <input type="date" id="expiration_date" bind:value={food.expiration_date} style='border-radius: 8px; margin-top:2px' class="w-full p-2"/>
                </div>
                <div class="flex flex-col w-1/2 p-2">
                    <label for="purchase_date" class="font-PoetsenOne">Purchase Date</label>
                    <input type="date" id="purchase_date" bind:value={food.purchase_date} style='border-radius: 8px; margin-top:2px' class="w-full p-2"/>
                </div>
            </div>
            <div class="flex justify-end p-2">
                <Button type="submit" class="flex font-PoetsenOne text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>SAVE</Button>
            </div>
        </form>
    </div>
</div>
{/if} -->

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
