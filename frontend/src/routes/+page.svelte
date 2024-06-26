<script>
    import { Card, Input, Label, Button, Select } from 'flowbite-svelte';
    import ModalDetail from './modal_detail.svelte';
    import ModalEdit from './modal_edit.svelte';
    import { onMount } from 'svelte';
    import { fetchData } from "$lib/fetchData.js";
    import LoadingPage from './loading.svelte';

    let categories = [];
    let activeCategories = [];
    let foodItems = [];
    let units = [];
    let isLoading = true;
    let error = null;

    onMount(async () => {
        try {
            // Fetch categories
            const categoriesResponse = await fetchData('foods/categories', 'GET');
            categories = categoriesResponse;
            activeCategories = categories.filter(category => category.isactive);

            // Fetch food items
            const foodItemsResponse = await fetchData('foods/fooditems', 'GET');
            console.log('Fetched food items:', foodItemsResponse); 
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
        const today = new Date();
        const expirationDate = new Date(expiration_date);
        const diffTime = expirationDate - today;
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        console.log('diffDays:', diffDays);
        if (diffDays < 0) {
            return 'text-red-500';
        } else if (diffDays <= 4) {
            return 'text-blue-500';
        } else {
            return 'text-black';
        }
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
        console.log('Showing food details:', food.id);
        selectedFood = food; // 선택된 식품 정보를 설정
    }

    function closeFoodDetails() {
        selectedFood = null; // 선택된 식품 정보를 null로 설정하여 모달 닫기
    }

    async function deleteFood(food) {
        try {
            const response = await fetchData(`foods/fooditems/${food.id}`, 'DELETE');
            if (response === null) {
                // 204 응답인 경우, response는 null입니다.
                foodItems = foodItems.filter(item => item.id !== food.id);
                closeFoodDetails();
            } else {
                console.error('Failed to delete food item');
            }
        } catch (err) {
            console.error('Error deleting item:', err);
        }
    }

    let editSelectedFood = '';

    function showEditForm(food) {
        editSelectedFood = food;
        closeFoodDetails();
    }

    async function editFood(food) {
        try {
            const response = await fetchData(`foods/fooditems/${food.id}`, 'PUT', food);
            if (response) {
                const index = foodItems.findIndex(item => item.id === food.id);
                foodItems[index] = response;
                closeEditForm();
            } else {
                console.error('Failed to update food item');
            }
        } catch (err) {
            console.error('Error updating item:', err);
        }
    }

    function closeEditForm() {
        editSelectedFood = '';
    }

    function scrollToCategory(categoryId) {
        const categoryElement = categoryRefs.get(categoryId);
        if (categoryElement) {
        categoryElement.scrollIntoView({ behavior: 'smooth' });
        }
    }




</script>


{#if isLoading}
    <LoadingPage/>
{:else if error}
    <b>Error: {error.message}</b>
{:else}
    {#each activeCategories  as category}
        <div class='bg-zinc-50/70 flex flex-col mb-5 overflow-hidden border rounded-xl shadow-md'>
            <div class="flex justify-center items-center px-4 py-4">
                <div class='flex items-center'>
                    <img src={category.img_url} class="h-6 sm:h-5" alt="ICON" />
                    <p class="font-grandstander text-xl md:text-lg sm: text-md font-bold text-amber-950 ml-2 mt-2"> {category.name}</p>
                </div>
            </div>
            <div class="mx-4 border-b border-zinc-950 border-opacity-30"></div>
            <div class="flex flex-wrap mx-4 my-2">
                {#each foodItems.filter(food => food.category_id === category.id) as food}
                    <div class="w-1/3 p-1 hover:bg-zinc-200 rounded-lg">
                        <button on:click={() => showFoodDetails(food)} class="relative border-1 border-opacity-30 border-lime-950 rounded-lg h-full w-full flex items-center justify-center p-2 focus:outline-none h-full">
                            <!-- <Card class="relative border-1 border-lime-950 rounded-lg h-full flex items-center justify-center"> -->
                                <div class="flex flex-col justify-center items-center text-center sm: p-1">
                                    <p class="font-PoetsenOne text-lime-950 font-semibold text-lg sm: text-xs sm: text-pretty">
                                        {food.foodname} <span class="whitespace-nowrap ">{food.volume}{getUnitName(food.unit_id)}</span>
                                    </p>
                                    <p class="{isExpired(food.expiration_date)} text-xs font-PoetsenOne whitespace-nowrap sm:text-xxs">
                                        {food.expiration_date}
                                    </p>
                                </div>
                            <!-- </Card>   -->
                        </button>
                    </div>
                {/each}
                <div class="w-1/3 p-1 hover:bg-zinc-200 rounded-lg">
                    <button on:click={toggleFormVisibility} class="cursor-pointer w-full relative bg-white border-1 border-lime-950 rounded-lg focus:outline-none h-full  " style="background-color: transparent;">
                        <!-- <Card class="relative border-1 border-lime-950 rounded-lg h-full flex items-center justify-center"> -->
                            <div class="flex flex-col justify-center items-center text-center p-2 sm:p-1">
                                <p class="font-PoetsenOne text-lime-950 font-semibold text-lg">
                                    +
                                </p>
                            </div>
                        <!-- </Card> -->
                    </button>
                </div>
            </div>
        </div>
    {/each}
{/if}


{#if selectedFood}
    <ModalDetail food={selectedFood} close={closeFoodDetails} {deleteFood} {showEditForm} {categories} {units}/>
{/if}



{#if editSelectedFood}
    <ModalEdit food={editSelectedFood} close={closeEditForm} {editFood} {categories} {units}/>
{/if}


<div class="modal {isFormVisible ? 'active' : ''}">
    <div class="modal-content relative " style="background-color: #FFFBF6;">
        <div class="flex justify-between items-center mb-2">
            <h2 class="text-lg font-grandstander ml-1"><strong>Add Food</strong></h2>
            <button on:click={toggleFormVisibility} class="text-lime-950 text-lg flex items-center ">&times;</button>
        </div>
        <div class="border-b border-zinc-950 border-opacity-30 mb-2"></div>
        <form on:submit|preventDefault={addItem}>
            <div class='flex flex-wrap -mx-2 p-2'>
                <label for="category" class="flex font-grandstander" style='font-size: 0.875rem;'>Category</label>
                <select id="category" bind:value={cat_selected} class="flex w-full p-2 border mt-1" style='border-radius: 8px; '>
                    {#each activeCategories as category}
                        <option value={category.id}>{category.name}</option>
                    {/each}
                </select>
            </div>
            <div class="flex flex-wrap -mx-2">
                <div class='flex flex-col w-1/3 p-2' style="min-height: 3rem;">
                    <label for="foodname" class="flex font-grandstander" style="font-size: 0.875rem;">Food Name</label>
                    <input type="text" bind:value={foodname} class='flex font-grandstander mt-1 h-full' style='border-radius: 8px;' required/>
                </div>
                <div class="flex flex-col w-1/3 p-2" style="min-height: 3rem;">
                    <label for="volume" class="flex font-grandstander" style="font-size: 0.875rem;">Volume</label>
                    <input type="number" id="volume" bind:value={volume} class="flex font-grandstander mt-1 h-full" style='border-radius: 8px;'/>
                </div>
                <div class="flex flex-col w-1/3 p-2" style="min-height: 3rem;">
                    <label for="unit" class="flex font-grandstander" style="font-size: 0.875rem;">Unit</label>
                    <select id="unit" bind:value={unit_selected} class="flex font-grandstander mt-1 h-full" style='border-radius: 8px;'>
                        {#each units as unit}
                            <option value={unit.id}>{unit.name}</option>
                        {/each}
                    </select>
                </div>
            </div>
            <div class="flex flex-wrap -mx-2">
                <div class="flex flex-col w-1/2 p-2">
                    <label for="purchase_date" class="font-grandstander">Purchase Date</label>
                    <input type="date" id="purchase_date" bind:value={purchaseDate} class="w-full p-2" style='border-radius: 8px; margin-top:2px; font-size: 0.875rem;'/>
                </div>
                <div class="flex flex-col w-1/2 p-2">
                    <label for="expiration_date" class="font-grandstander">Expiration Date</label>
                    <input type="date" id="expiration_date" bind:value={expirationDate} class="w-full p-2" style='border-radius: 8px; margin-top:2px;font-size: 0.875rem;'/>
                </div>
            </div>
            <div class='flex justify-end mt-2'>
                <Button type="submit" class="flex border-[1px] border-zinc-500 text-xxs font-semibold font-PoetsenOne  bg-[#E8C9D5]/50 text-zinc-950 hover:bg-[#E8C9D5]" size='xs'>ADD</Button>
            </div>
        </form>
    </div>
</div>


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