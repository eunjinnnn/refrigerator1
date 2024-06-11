<script>
    import { Button } from 'flowbite-svelte';
    export let food;
    export let close;
    export let editFood;
    export let categories; // 카테고리 리스트
    export let units; // 단위 리스트


    // food.category ID에 해당하는 카테고리 이름을 가져오는 함수
    function getCategoryName(categoryId) {
        const category = categories.find(cat => cat.id === categoryId);
        return category ? category.name : 'Unknown';
    }

</script>


{#if food}
<div class="modal active">
    <div class="bg-orange-50 rounded-lg p-4 w-full sm:w-1/2 modal-content" style="background-color: #FFFBF6;">
        <div class="flex justify-between items-center mb-2">
            <h2 class="text-lg sm:text-base text-lime-950 font-grandstander"><strong>Edit Food</strong></h2>
            <button on:click={close} class="text-lime-950 text-lg sm:text-base flex items-center">&times;</button>
        </div>

        <div class="border-b border-lime-950 border-opacity-30 mb-2"></div>

        <form on:submit={() => editFood(food)}>
            <div class="flex flex-col mt-2 p-2">
                <label for="category" class="flex font-grandstander" style="font-size: 0.875rem;">Category</label>
                <select id="category" bind:value={food.category_id} class="flex w-full p-2 mt-1 border-opacity-30" style='border-radius: 8px;'>
                    {#each categories as category}
                        <option value={category.id}>{category.name}</option>
                    {/each}
                </select>
            </div>
            <div class='flex flex-wrap'>
                <div class='flex flex-col w-1/3 p-2' style="min-height: 3rem;">
                    <label for="foodname" class="flex font-grandstander whitespace-nowrap" style="font-size: 0.875rem;">Food Name</label>
                    <input type="text" bind:value={food.foodname} class='flex font-PoetsenOne mt-1 h-full text-no' style='border-radius: 8px;' id="foodname" placeholder="Foodname" required/>
                </div>
                <div class="flex flex-col w-1/3 p-2" style="min-height: 3rem;">
                    <label for="volume" class="flex font-grandstander" style="font-size: 0.875rem;">Volume</label>
                    <input type="number" id="volume" bind:value={food.volume} class="flex font-PoetsenOne mt-1 h-full" style='border-radius: 8px;'/>
                </div>
                <div class="flex flex-col w-1/3 p-2" style="min-height: 3rem;">
                    <label for="unit" class="flex font-grandstander" style="font-size: 0.875rem;">Unit</label>
                    <select id="unit" bind:value={food.unit_id} class="flex font-PoetsenOne mt-1 h-full" style='border-radius: 8px;'>
                        {#each units as unit}
                            <option value={unit.id}>{unit.name}</option>
                        {/each}
                    </select>
                </div>
            </div>
            <div class="flex flex-wrap">
                <div class="flex flex-col w-1/2 p-2">
                    <label for="expiration_date" class="font-grandstander whitespace-nowrap">Expiration Date</label>
                    <input type="date" id="expiration_date" bind:value={food.expiration_date} class="w-full p-2" style='border-radius: 8px; margin-top:2px; font-size: 0.875rem;'/>
                </div>
                <div class="flex flex-col w-1/2 p-2">
                    <label for="purchase_date" class="font-grandstander">Purchase Date</label>
                    <input type="date" id="purchase_date" bind:value={food.purchase_date} class="w-full p-2" style='border-radius: 8px; margin-top:2px; font-size: 0.875rem;'/>
                </div>
            </div>
            <div class="flex justify-end p-2">
                <Button type="submit" class="flex border-[1px] border-zinc-500 text-xxs font-semibold font-PoetsenOne  bg-[#E8C9D5]/50 text-zinc-950 hover:bg-[#E8C9D5]" size='xs'>SAVE</Button>
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