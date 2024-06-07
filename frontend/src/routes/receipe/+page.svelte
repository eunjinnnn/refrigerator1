<!-- <script>
    import { onMount } from 'svelte';
    import { fetchData } from "$lib/fetchData.js";

    let categories = [];

    onMount(async () => {
        try {
            const response = await fetchData("foods/categories", "GET");
            categories = response;
        } catch (error) {
            console.error("Error fetching categories:", error);
        }
    });
</script>

<div class="mt-16 px-3">
    {#if categories.length === 0}
        <b>Loading...</b>
    {:else}
        {#each categories as category}
            <div>
                <img src={category.img_url} class="h-6 sm:h-5" alt="ICON" />
                <b>{category.name}</b>
            </div>
        {/each}
    {/if}
</div> -->
<script>
    import { onMount } from 'svelte';
    import { fetchData } from '$lib/fetchData.js';

    let categories = [];
    let foodItems = [];
    let units = [];
    let isLoading = true;
    /**
     * @type {unknown}
     */
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
</script>

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
                </div>
                <div class="mx-4 border-b border-lime-950 border-opacity-30"></div>
                <div class="flex flex-wrap mx-4 my-2">
                    {#each foodItems.filter(food => food.category_id === category.id) as food}
                        <div class="w-1/3 p-1">
                            <div class="cursor-pointer w-full relative bg-white border-1 border-lime-950 rounded-lg focus:outline-none">
                                <div class="relative border-1 border-lime-950 rounded-lg">
                                    <div class="flex flex-col justify-center items-center">
                                        <p class="font-PoetsenOne text-sm text-lime-950 font-semibold whitespace-nowrap sm: text-xs sm: text-pretty">
                                            {food.foodname} {food.volume} {getUnitName(food.unit_id)}
                                        </p>
                                        <p class="{new Date(food.expiration_date) < new Date() ? 'text-red-500' : 'text-lime-950'} text-xs font-PoetsenOne sm: text-xxs">
                                            {food.expiration_date}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    {/each}
                </div>
            </div>
        {/each}
    </div>
{/if}
