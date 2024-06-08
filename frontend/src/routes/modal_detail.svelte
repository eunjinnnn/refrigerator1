<script>
    import { Button, Label, Input, Select } from 'flowbite-svelte';
    export let food;
    export let close;
    export let deleteFood;
    export let editFood;

    let showEditModal = false;

    let categories = [
        { id: 1, name: 'VEGETABLES' },
        { id: 2, name: 'DRINKS' },
        { id: 3, name: 'FROZEN FOOD' },
        { id: 4, name: 'ETC' }
    ];

    let units = [
        { value: 1, name: '개' },
        { value: 2, name: 'L' },
        { value: 3, name: '조각' }
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
    
    // async function editFood(event) {
    //     event.preventDefault();
        
    //     // 여기서 필요한 경우 서버에 수정된 데이터를 전송하는 코드를 작성합니다.
    //     // 예시: await fetch('/api/food', { method: 'PUT', body: JSON.stringify(food), headers: { 'Content-Type': 'application/json' } });
        
    //     console.log('Edited food:', food);
        
    //     // 모달을 닫습니다.
    //     closeEditModal();
    // }
</script>

{#if food}
<div class="modal {food ? 'active' : ''}">
    <div class="bg-orange-50 rounded-lg p-4 w-1/2 modal-content">
        <div class="flex justify-between items-center mb-2">
            <h2 class="text-lg text-lime-950 font-PoetsenOne"><strong>{food.foodname} {food.volume}{food.unit}</strong></h2>
            <button on:click={close} class="text-lime-950 text-lg flex items-center ">&times;</button>
        </div>

        <div class="border-b border-lime-950 border-opacity-30 mb-2"></div>
        <p class='font-PoetsenOne'><strong>Category:</strong> {getCategoryName(food.category)}</p>
        <p class='font-PoetsenOne'><strong>Purchase Date:</strong> {food.purchase_date}</p>
        <p class='font-PoetsenOne'><strong>Expiration Date:</strong> {food.expiration_date}</p>
        <div class='flex justify-between mt-2'>
            <Button type="button" on:click={() => deleteFood(food)} class="flex font-PoetsenOne text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>DELETE</Button>
            <Button type="button" on:click={openEditModal} class="flex font-PoetsenOne text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>EDIT</Button>
        </div>
    </div>
</div>
{/if}

<!-- {#if showEditModal}
<div class="modal active">
    <div class="bg-orange-50 rounded-lg p-4 w-1/2 modal-content">
        <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg text-lime-950 font-PoetsenOne"><strong>Edit Food</strong></h2>
            <button on:click={closeEditModal} class="text-lime-950 text-lg flex items-center ">&times;</button>
        </div>

        <div class="border-b border-lime-950 border-opacity-30 mb-2"></div>

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
{/if} -->


{#if showEditModal}
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
                <select id="category" bind:value={food.category} class="flex w-full p-2 mt-1 border-opacity-30" style='border-radius: 8px;' >
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
                    <select id="unit" bind:value={food.unit} style='border-radius: 8px;' class="flex font-PoetsenOne mt-1">
                        {#each units as unit}
                            <option value={unit.value}>{unit.name}</option>
                        {/each}
                    </select>
                </div>
            </div>
            <div class="flex flex-wrap">
                <div class="flex flex-col w-1/2 p-2">
                    <label for="expiration_date" class="font-PoetsenOne">Expiration Date</label>
                    <input type="date" id="expiration_date" bind:value={food.purchase_date} style='border-radius: 8px; margin-top:2px' class="w-full p-2"/>
                </div>
                <div class="flex flex-col w-1/2 p-2">
                    <label for="purchase_date" class="font-PoetsenOne">Purchase Date</label>
                    <input type="date" id="purchase_date" bind:value={food.expiration_date} style='border-radius: 8px; margin-top:2px' class="w-full p-2"/>
                </div>
            </div>
            <div class="flex justify-end p-2">
                <Button type="submit" class="flex font-PoetsenOne text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>SAVE</Button>
            </div>
        </form>
    </div>
</div>
{/if}

    <!-- <div class="modal active">
        <div class="modal-content relative"> 
            <button on:click={closeEditModal} class="absolute top-0 right-0 mt-2 mr-2 text-lime-950 text-lg">&times;</button> 
            <form on:submit|preventDefault={editFood} > 
                <div class='flex flex-wrap -mx-2 p-2'>
                    <Label for="Category" class="mb-2 text-xs">Category</Label>
                    <Select id="select-category" bind:value={food.category} style='font-size:x-small' size="sm" items={categories} placeholder="Category"/>
                </div>
                <div class="flex flex-wrap -mx-2">
                    <div class='flex flex-col w-1/3 p-2'>
                        <Label for="Foodname" class="mb-2 text-xs">Foodname</Label>
                        <Input type="text" bind:value={food.foodname} class='border rounded border-gray-300' id="foodname" style='font-size:x-small' placeholder="Foodname" required/>
                    </div>
                    <div class='flex flex-col w-1/3 p-2'>
                        <Label for="Volume" class="mb-2 text-xs">Volume</Label>
                        <Input type="number" bind:value={food.volume} class='rounded' id="volume" style='font-size:x-small' placeholder="Volume" required />
                    </div>
                    <div class='flex flex-col w-1/3 p-2'>
                        <Label for="Unit" class="mb-2 text-xs">Unit</Label>
                        <Select id="select-unit" bind:value={food.unit} class='' size="md" style='font-size:x-small' items={units} placeholder="Unit"/>
                    </div>
                </div>
                <div class="flex flex-wrap -mx-2">
                    <div class='flex flex-col w-1/2 p-2'>
                        <Label for="purchaseDate" class="mb-2 text-xs">Purchase Date</Label>
                        <Input type="date" bind:value={food.purchase_date} class='' style='font-size:x-small' id="purchaseDate" required />
                    </div>
                    <div class='flex flex-col w-1/2 p-2'>
                        <Label for="expirationDate" class="mb-2 text-xs">Expiration date</Label>
                        <Input type="date" bind:value={food.expiration_date} class='' id="expirationDate" style='font-size:x-small' required />
                    </div>
                </div>
                <div class='flex justify-between'>
                    <Button type="submit" class="flex text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>Save</Button>
                </div>
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
