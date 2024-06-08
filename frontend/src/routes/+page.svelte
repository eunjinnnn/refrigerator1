<script>
    import { Card, Input, Label, Button, Select } from 'flowbite-svelte';
    import ModalDetail from './modal_detail.svelte';
    import { onMount } from 'svelte';
    import { fetchData } from "$lib/fetchData.js";

    let categories = [];
    let foodItems = [];
    let units = [];
    let isLoading = true;
    let error = null;

    onMount(async () => {
        try {
            // Fetch categories
            const categoriesResponse = await fetchData('foods/categories', 'GET');
            categories = categoriesResponse;

            // Fetch food items
            const foodItemsResponse = await fetchData('foods/fooditems', 'GET');
            foodItems = foodItemsResponse;

            // Fetch units
            const unitsResponse = await fetchData('foods/foodunits', 'GET');
            units = unitsResponse;

            isLoading = false;
        } catch (err) {
            error = err;
            isLoading = false;
        }
    });

    function getUnitName(unitId) {
        const unit = units.find(unit => unit.id === unitId);
        return unit ? unit.name : '';
    }

    function getCategoryName(categoryId) {
        const category = categories.find(cat => cat.id === categoryId);
        return category ? category.name : 'Unknown';
    }

    // 폼 데이터 상태 변수
    let cat_selected = '';
    let foodname = '';
    let volume = '';
    let unit_selected = '';
    let expirationDate = '';
    let purchaseDate = '';

    // 모달 상태 변수
    let isFormVisible = false;

    // function filteredItems(categoryId) {
    //     return item_list.filter(item => item.category === categoryId).sort((a, b) => {
    //         return new Date(a.expiration_date) - new Date(b.expiration_date);
    //     });
    // }

    // ADD FOOD 관련 함수 
    // 유통기한 지난 날짜 빨간색으로 표시
    function isExpired(expiration_date) {
        return new Date(expiration_date) < new Date();
    }

    // 버튼 누르면 ADD FORM MODAL 띄우기
    function toggleFormVisibility() {
        isFormVisible = !isFormVisible;
    }

    // ADD FORM에서 SUBMIT 버튼 누르면 실행
    async function addItem(event) {
        event.preventDefault();
        try {
            const newItem = {
                category_id: parseInt(cat_selected) || 0,
                foodname: foodname,
                volume: parseInt(volume) || 0,
                unit_id: parseInt(unit_selected) || 0,
                expiration_date: expirationDate,
                purchase_date: purchaseDate
            };

            // 데이터가 올바르게 포맷되었는지 콘솔에 출력하여 확인
            console.log("newItem:", JSON.stringify(newItem, null, 2));

            const response = await fetchData('foods/fooditems', 'POST', newItem);

            // 성공적으로 저장된 경우 foodItems 배열에 추가
            foodItems = [...foodItems, response]; // 새로운 배열을 할당

            // 폼 초기화 및 모달 닫기
            cat_selected = '';
            foodname = '';
            volume = '';
            unit_selected = '';
            expirationDate = '';
            purchaseDate = '';
            toggleFormVisibility();
        } catch (err) {
            console.error('Error adding item:', err);
        }
}

    let selectedFood = null; // 선택된 식품 정보를 저장하는 writable store
    let isAddVisible = false;
    
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
    body {
    overflow-x: hidden; /* Prevent horizontal scroll */
  }
</style>

{#if isLoading}
    <b>Loading...</b>
{:else if error}
    <b>Error: {error.message}</b>
{:else}
    <div class="mt-16 px-3">
        {#each categories as category}
            <div class='bg-neutral-50/70 flex flex-col mb-5 overflow-hidden border rounded-xl shadow-md'>
                <div class="flex justify-center items-center px-4 py-4">
                    <div class='flex items-center'>
                        <img src={category.img_url} class="h-6 sm:h-5" alt="ICON" />
                        <p class="font-PoetsenOne text-lg font-bold text-lime-950 ml-2"> {category.name}</p>
                    </div>
                    <div>
                        <a href="#" on:click|preventDefault={toggleFormVisibility} class="font-serif text-lime-950 text-sm font-medium text-primary-600"> + </a>
                    </div>
                </div>
                <div class="mx-4 border-b border-lime-950 border-opacity-30"></div>
                <div class="flex flex-wrap mx-4 my-2">
                    {#each foodItems.filter(food => food.category_id === category.id) as food}
                        <div class="w-1/3 p-1">
                            <button on:click={() => showFoodDetails(food)} class="cursor-pointer w-full relative bg-white border-1 border-lime-950 rounded-lg focus:outline-none">
                                <Card class="relative border-1 border-lime-950 rounded-lg">
                                    <div class="flex flex-col justify-center items-center">
                                        <p class="font-PoetsenOne text-sm text-lime-950 font-semibold whitespace-nowrap sm: text-xs sm: text-pretty">
                                            {food.foodname} {food.volume} {getUnitName(food.unit_id)}
                                        </p>
                                        <p class="{isExpired(food.expiration_date) ? 'text-red-500' : 'text-lime-950'} text-xs font-PoetsenOne sm: text-xxs">
                                            {food.expiration_date}
                                        </p>
                                    </div>
                                </Card>
                            </button>
                        </div>
                    {/each}
                </div>
            </div>
        {/each}
    </div>
{/if}

{#if selectedFood}
    <ModalDetail food={selectedFood} close={closeFoodDetails} {deleteFood} {showEditForm} {categories} {units}/>
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
                            <option value={unit.id}>{unit.name}</option>
                        {/each}
                    </select>
                </div>
            </div>
            <div class="flex flex-wrap -mx-2">
                <div class="flex flex-col w-1/2 p-2">
                    <label for="purchase_date" class="font-PoetsenOne">Purchase Date</label>
                    <input type="date" id="purchase_date" bind:value={purchaseDate} style='border-radius: 8px; margin-top:2px' class="w-full p-2"/>
                </div>
                <div class="flex flex-col w-1/2 p-2">
                    <label for="expiration_date" class="font-PoetsenOne">Expiration Date</label>
                    <input type="date" id="expiration_date" bind:value={expirationDate} style='border-radius: 8px; margin-top:2px' class="w-full p-2"/>
                </div>
            </div>
            <div class='flex justify-end mt-2'>
                <Button type="submit" class="flex text-xxs bg-lime-950 text-orange-50 hover:text-lime-950 hover:bg-lime-800" size='xs'>ADD</Button>
            </div>
        </form>
    </div>
</div>

