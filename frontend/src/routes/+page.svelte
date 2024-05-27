<script>
    import { Card, Input, Label, Button, Select } from 'flowbite-svelte';
    import Modal from './modal_detail.svelte';

    let categories = [
        { id: 1, name: 'VEGETABLES' },
        { id: 2, name: 'DRINKS' },
        { id: 3, name: 'FROZEN FOOD' },
        { id: 4, name: 'ETC' }
    ];

    let item_list = [
        { category: 1, foodname: '양파', volume: '5', unit: '개', expiration_date: '2024-05-24', purchase_date: '2024-05-20' },
        { category: 1, foodname: '대파', volume: '5', unit: '개', expiration_date: '2024-05-23',  purchase_date: '2024-05-20' },
        { category: 1, foodname: '당근', volume: '5', unit: '개', expiration_date: '2024-05-05', purchase_date: '2024-05-20' },
        { category: 1, foodname: '양배추', volume: '5', unit: '개', expiration_date: '2024-05-07', purchase_date: '2024-05-20' },
        { category: 2, foodname: '사이다', volume: '2', unit: 'L', expiration_date: '2024-05-28', purchase_date: '2024-05-20' },
        { category: 2, foodname: '콜라', volume: '2', unit: 'L', expiration_date: '2024-05-06', purchase_date: '2024-05-20' },
        { category: 3, foodname: '만두', volume: '2', unit: '개', expiration_date: '2024-05-06', purchase_date: '2024-05-20' },
        { category: 4, foodname: '다진마늘', volume: '10', unit: '조각', expiration_date: '2025-05-06', purchase_date: '2024-05-20' },
    ];

    let units = [
        { value: 1, name: '개' },
        { value: 2, name: 'L' },
        { value: 3, name: '조각' }
    ];

    let lists = [];
    let cat_selected = '';
    let unit_selected = '';
    let volume = '';
    let foodname = '';
    let purchaseDate = '';
    let expirationDate = '';
    let isFormVisible = false;

    /**
     * @type {string | null}
     */
    let selectedFood = null; // 선택된 식품 정보를 저장하는 writable store

    /**
     * @param {number} categoryId
     */
    function filteredItems(categoryId) {
        return item_list.filter(item => item.category === categoryId).sort((a, b) => {
            return new Date(a.expiration_date) - new Date(b.expiration_date);
        });
    }

    function isExpired(expiration_date) {
        return new Date(expiration_date) < new Date();
    }

    function toggleFormVisibility() {
        isFormVisible = !isFormVisible;
    }

    function addItem(event) {
        event.preventDefault();
        const selectedCategory = categories.find(cat => cat.value == cat_selected)?.name || '';
        const selectedUnit = units.find(unit => unit.value == unit_selected)?.name || '';

        lists.push({
            foodname,
            volume,
            unit: selectedUnit,
            category: selectedCategory,
            purchaseDate,
            expirationDate
        });

        foodname = '';
        volume = '';
        unit_selected = '';
        cat_selected = '';
        purchaseDate = '';
        expirationDate = '';
    }

    function showFoodDetails(food) {
        selectedFood = food; // 선택된 식품 정보를 설정
    }

    function closeFoodDetails() {
        selectedFood = null; // 선택된 식품 정보를 null로 설정하여 모달 닫기
    }
</script>


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
        /* transition: visibility 0s, opacity 0.5s linear; */
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


{#each categories as category}
    <div class='bg-orange-50 mt-2 mb-2 container mx-auto rounded border-dashed border-lime-950 overflow-hidden'>
        <div class="flex justify-between items-center px-4 py-2">
            <p class="font-PoetsenOne text-sm font-semibold text-lime-950 truncate dark:text-white"># {category.name}</p>
            <div>
                <a href="#" on:click|preventDefault={toggleFormVisibility} class="font-serif text-lime-950 text-sm font-medium text-primary-600"> + </a>
            </div>
        </div>
        <div class="border-b border-lime-950 border-opacity-30"></div>
        <div class="flex flex-wrap mt-2">
            {#each filteredItems(category.id) as food}
                <div class="w-1/3 p-1">
                    <button on:click={() => showFoodDetails(food)} class="cursor-pointer w-full relative bg-white border-1 border-lime-950 rounded-lg focus:outline-none">
                        <Card class="w-full relative bg-white border-1 border-lime-950 rounded-lg">
                            <div class="flex flex-col justify-center items-center">
                                <p class="font-PoetsenOne text-xs text-lime-950 font-bold whitespace-nowrap">{food.foodname} {food.volume}{food.unit}</p>
                                <p class="{isExpired(food.expiration_date) ? 'text-red-500' : 'text-lime-950'} text-xs font-PoetsenOne">{food.expiration_date}</p>
                            </div>
                        </Card>
                    </button>
                </div>
            {/each}
        </div>
    </div>
{/each}

{#if selectedFood}
    <Modal food={selectedFood} close={closeFoodDetails} />
{/if}



<!-- modal -->
<div class="modal {isFormVisible ? 'active' : ''}">
    <div class="modal-content">
        <form on:submit|preventDefault={addItem}>
            <div class='flex flex-wrap -mx-2 p-2'>
                <Label for="Category" class="mb-2 text-xs">Category</Label>
                <Select id="select-category" bind:value={cat_selected} style='font-size:x-small' size="sm" items={categories} placeholder="Category"/>
            </div>
            <div class="flex flex-wrap -mx-2">
                <div class='flex flex-col w-1/3 p-2'>
                    <Label for="Foodname" class="mb-2 text-xs">Foodname</Label>
                    <Input type="text" bind:value={foodname} class='border rounded border-gray-300' id="foodname" style='font-size:x-small' placeholder="Foodname" required/>
                </div>
                <div class='flex flex-col w-1/3 p-2'>
                    <Label for="Volume" class="mb-2 text-xs">Volume</Label>
                    <Input type="number" bind:value={volume} class='rounded' id="volume" style='font-size:x-small' placeholder="Volume" required />
                </div>
                <div class='flex flex-col w-1/3 p-2'>
                    <Label for="Unit" class="mb-2 text-xs">Unit</Label>
                    <Select id="select-unit" bind:value={unit_selected} class='' size="md" style='font-size:x-small' items={units} placeholder="Unit"/>
                </div>
            </div>
            <div class="flex flex-wrap -mx-2">
                <div class='flex flex-col w-1/2 p-2'>
                    <Label for="purchaseDate" class="mb-2 text-xs">Purchase Date</Label>
                    <Input type="date" bind:value={purchaseDate} class='' style='font-size:x-small' id="purchaseDate" required />
                </div>
                <div class='flex flex-col w-1/2 p-2'>
                    <Label for="expirationDate" class="mb-2 text-xs">Expiration date</Label>
                    <Input type="date" bind:value={expirationDate} class='' id="expirationDate" style='font-size:x-small' required />
                </div>
            </div>
            <div class= 'flex justify-between'>
                <Button type="button" on:click={toggleFormVisibility} class="flex text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>BACK</Button>
                <Button type="submit" class="flex text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size = 'xs'>ADD</Button>
            </div>
        </form>
    </div>
</div>

