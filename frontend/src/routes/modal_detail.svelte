<script>
    import { Button } from 'flowbite-svelte';
    export let food;
    export let close;
    export let deleteFood;
    export let editFood;

    let showEditModal = false; // 새로운 모달의 상태

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

    function openEditModal() {
        showEditModal = true;
    }

    function closeEditModal() {
        showEditModal = false;
    }
    
    async function editFood(event) {
        event.preventDefault();
        
        // 여기서 필요한 경우 서버에 수정된 데이터를 전송하는 코드를 작성합니다.
        // 예시: await fetch('/api/food', { method: 'PUT', body: JSON.stringify(food), headers: { 'Content-Type': 'application/json' } });
        
        console.log('Edited food:', food);
        
        // 모달을 닫습니다.
        closeEditModal();
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
            <Button type="button" on:click={openEditModal} class="flex font-PoetsenOne text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>EDIT</Button>
        </div>
    </div>
</div>
{/if}

{#if showEditModal}
<div class="modal active">
    <div class="bg-orange-50 rounded-lg p-4 w-1/2 modal-content">
        <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg text-lime-950 font-PoetsenOne"><strong>Edit Food</strong></h2>
            <button on:click={closeEditModal} class="text-lime-950 text-lg flex items-center ">&times;</button>
        </div>

        <div class="border-b border-lime-950 border-opacity-30 mb-2"></div>
        <!-- EDIT FORM CONTENT HERE -->
        <form on:submit={editFood}>
            <div>
                <label for="foodname" class="font-PoetsenOne"><strong>Food Name:</strong></label>
                <input type="text" id="foodname" bind:value={food.foodname} class="w-full p-2 border rounded"/>
            </div>
            <div class="mt-2">
                <label for="category" class="font-PoetsenOne"><strong>Category:</strong></label>
                <select id="category" bind:value={food.category} class="w-full p-2 border rounded">
                    {#each categories as category}
                        <option value={category.id}>{category.name}</option>
                    {/each}
                </select>
            </div>
            <div class="mt-2">
                <label for="volume" class="font-PoetsenOne"><strong>Volume:</strong></label>
                <input type="number" id="volume" bind:value={food.volume} class="w-full p-2 border rounded"/>
            </div>
            <div class="mt-2">
                <label for="unit" class="font-PoetsenOne"><strong>Unit:</strong></label>
                <input type="text" id="unit" bind:value={food.unit} class="w-full p-2 border rounded"/>
            </div>
            <div class="mt-2">
                <label for="expiration_date" class="font-PoetsenOne"><strong>Expiration Date:</strong></label>
                <input type="date" id="expiration_date" bind:value={food.expiration_date} class="w-full p-2 border rounded"/>
            </div>
            <div class="mt-2">
                <label for="purchase_date" class="font-PoetsenOne"><strong>Purchase Date:</strong></label>
                <input type="date" id="purchase_date" bind:value={food.purchase_date} class="w-full p-2 border rounded"/>
            </div>
            <div class="flex justify-end mt-4">
                <Button type="submit" class="flex font-PoetsenOne text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>SAVE</Button>
            </div>
        </form>
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
