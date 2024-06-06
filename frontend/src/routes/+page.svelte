<script>
    import { Card, Input, Label, Button, Select } from 'flowbite-svelte';
    import ModalDetail from './modal_detail.svelte';

    let categories = [
        { id: 1, name: 'VEGETABLES', img_url: '/images/vegetable_icon.png'},
        { id: 2, name: 'DRINKS', img_url: '/images/drinks_icon.png'},
        { id: 3, name: 'FROZEN FOOD', img_url: '/images/frozen_food_icon.png'},
        { id: 4, name: 'ETC', img_url: '/images/etc_icon.png'}
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
    let selectedFood = null; // 선택된 식품 정보를 저장하는 writable store
    let isAddVisible = false;
    // let isEditVisible = false

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
        toggleFormVisibility();
    }

    function showFoodDetails(food) {
        selectedFood = food; // 선택된 식품 정보를 설정
    }

    function closeFoodDetails() {
        selectedFood = null; // 선택된 식품 정보를 null로 설정하여 모달 닫기
    }

    function deleteFood(food) {
        item_list = item_list.filter(item => item !== food);
        closeFoodDetails(); // Close the modal after deletion
    }

    function showEditForm(food) {
        selectedFood = food;
        cat_selected = categories.find(cat => cat.value == food.category)?.name || '';
        unit_selected = units.find(unit => unit.value == food.unit)?.name || '';
        volume = food.volume;
        foodname = food.foodname;
        purchaseDate = food.purchase_date;
        expirationDate = food.expiration_date;
        isFormVisible = true;
        console.log(isFormVisible)
    }

    function addListVisibility() {
        isAddVisible = !isAddVisible;
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
    <div class='bg-orange-50[.6] flex flex-col mb-2 overflow-hidden'>
        <div class="flex justify-between items-center px-4 py-2">
            <div class = 'flex justify-between items-center'>
                <img src={category.img_url} class="h-8 sm:h-10" alt="ICON" />
                <p class="font-PoetsenOne text-lg font-bold text-lime-950"> {category.name}</p>
            </div>
            <div>
                <a href="#" on:click|preventDefault={toggleFormVisibility} class="font-serif text-lime-950 text-sm font-medium text-primary-600"> + </a>
            </div>
        </div>
        <div class="border-b border-lime-950 border-opacity-30"></div>
        <div class="flex flex-wrap mt-2">
            {#each filteredItems(category.id) as food}
                <div class="w-1/3 p-1">
                    <button on:click={() => showFoodDetails(food)} class="cursor-pointer w-full relative bg-white border-1 border-lime-950 rounded-lg focus:outline-none">
                        <Card class="relative border-1 border-lime-950 rounded-lg">
                            <div class="flex flex-col justify-center items-center">
                                <p class="font-PoetsenOne text-sm text-lime-950 font-semibold whitespace-nowrap">{food.foodname} {food.volume}{food.unit}</p>
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
    <ModalDetail food={selectedFood} close={closeFoodDetails} {deleteFood} {showEditForm}/>
{/if}

<!-- {#if isEditVisible}
    <div>hi</div>
{/if} -->
<!-- svelte-ignore empty-block -->
<!-- {#if isAddVisible}
    <div> hi </div>
{:else}
    <Button type="button" on:click={addListVisibility} class="flex text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='sm'>TODAY'S COOKING</Button>
{/if} -->


<!-- modal -->
<div class="modal {isFormVisible ? 'active' : ''}">
    <div class="modal-content relative"> <!-- relative 클래스 추가 -->
        <div class="flex justify-between items-center mb-2">
            <h2 class="text-lg text-lime-950 font-PoetsenOne"><strong>Add Food</strong></h2>
            <button on:click={toggleFormVisibility} class="text-lime-950 text-lg flex items-center ">&times;</button>
        </div>
        
        <form on:submit|preventDefault={addItem} > <!-- 버튼과 겹치지 않게 margin-top 추가 -->
            <div class='flex flex-wrap -mx-2 p-2'>
                <label for="category" class="flex font-PoetsenOne">Category</label>
                <select id="category" bind:value={cat_selected} class="flex w-full p-2 border mt-1" style='border-radius: 8px;' >
                    {#each categories as category}
                        <option value={category.id}>{category.name}</option>
                    {/each}
                </select>
            </div>
            <div class="flex flex-wrap -mx-2">
                <div class='flex flex-col w-1/3 p-2'>
                    <label for="foodname" class="flex font-PoetsenOne">Food Name</label>
                    <input type="text" bind:value={foodname} class='flex font-PoetsenOne mt-1' style='border-radius: 8px;' id="foodname" placeholder="Foodname" required/>
                </div>
                <div class="flex flex-col w-1/3 p-2">
                    <label for="volume" class="flex font-PoetsenOne">Volume</label>
                    <input type="number" id="volume" bind:value={volume} style='border-radius: 8px;' class="flex font-PoetsenOne mt-1"/>
                </div>
                <div class="flex flex-col w-1/3 p-2">
                    <label for="unit" class="flex font-PoetsenOne">Unit</label>
                    <select id="unit" bind:value={unit_selected} style='border-radius: 8px;' class="flex font-PoetsenOne mt-1">
                        {#each units as unit}
                            <option value={unit.value}>{unit.name}</option>
                        {/each}
                    </select>
                </div>
            </div>
            <div class="flex flex-wrap -mx-2">
                <div class="flex flex-col w-1/2 p-2">
                    <label for="expiration_date" class="font-PoetsenOne">Expiration Date</label>
                    <input type="date" id="expiration_date" bind:value={purchaseDate} style='border-radius: 8px; margin-top:2px' class="w-full p-2"/>
                </div>
                <div class="flex flex-col w-1/2 p-2">
                    <label for="purchase_date" class="font-PoetsenOne">Purchase Date</label>
                    <input type="date" id="purchase_date" bind:value={expirationDate} style='border-radius: 8px; margin-top:2px' class="w-full p-2"/>
                </div>
            </div>
            <div class='flex justify-end mt-2'>
                <Button type="submit" class="flex text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>ADD</Button>
            </div>
        </form>
    </div>
</div>

