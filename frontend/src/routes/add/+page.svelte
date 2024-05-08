<script>
    import { Label, Select, Input, FloatingLabelInput } from 'flowbite-svelte';
    
    let cat_selected;
    let unit_selected;
    let volume;
    let foodname;
  
    let categories = [
        { value: 1, name: 'VEGETABLES' },
        { value: 2, name: 'DRINKS' },
        { value: 3, name: 'FROZEN FOOD' },
        { value: 4, name: 'ETC' }
    ];
  
    let units = [
        { value: 1, name: '개' },
        { value: 2, name: 'L' },
        { value: 3, name: '조각' }
    ];
  
    function handleCategoryChange(event) {=== parseInt(event.target.value));
    }
  
    function handleUnitChange(event) {
        unit_selected = units.find(unit => unit.value === parseInt(event.target.value));
    }
        cat_selected = categories.find(cat => cat.value 
  </script>
  
  <Label>
    <Select class="mt-2" on:change={handleCategoryChange}>
        {#each categories as category}
            <option value={category.value}>{category.value}</option>
        {/each}
    </Select>
    <div class="mt-2">
      <FloatingLabelInput bind:value={foodname} style="outlined" id="default_outlined" name="default_outlined" type="text">
          음식 이름
      </FloatingLabelInput>
    </div>
    <div class="mt-2">
      <FloatingLabelInput bind:value={volume} style="outlined" id="default_outlined" name="default_outlined" type="text">
        양
    </FloatingLabelInput>
    </div>
    <Select class="mt-2" on:change={handleUnitChange}>
        {#each units as unit}
            <option value={unit.value}>{unit.name}</option>
        {/each}
    </Select>
    <div class = 'flex '>
        <p>{cat_selected ? cat_selected.name : ''}</p>
        <p>{foodname}</p>
        <p>{volume}</p>
        <p>{unit_selected ? unit_selected.name : ''}</p>
    </div>
    
  </Label>
  